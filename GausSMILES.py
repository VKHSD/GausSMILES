from rdkit import Chem
from rdkit.Chem import AllChem


def smiles_to_graph(smiles):
    """
    Parses a SMILES string into a graph representation with bond orders.
    Returns an adjacency list with bond orders and a dictionary mapping atom indices to elements.
    """
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)

    if mol is None:
        raise ValueError("Invalid SMILES string")

    adjacency_list = {}
    atom_ids = {}

    for atom in mol.GetAtoms():
        idx = atom.GetIdx()
        symbol = atom.GetSymbol()
        atom_ids[idx] = symbol
        adjacency_list[idx] = []

    for bond in mol.GetBonds():
        a1, a2 = bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()
        bond_order = bond.GetBondTypeAsDouble()
        adjacency_list[a1].append((a2, bond_order))
        adjacency_list[a2].append((a1, bond_order))

    return adjacency_list, atom_ids


def smiles_to_3d_coordinates(smiles):
    """
    Generates approximate 3D coordinates for a molecule from a SMILES string.
    Returns a dictionary mapping atom IDs to 3D coordinates.
    """
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())
    AllChem.UFFOptimizeMolecule(mol)

    coordinates = {}
    conf = mol.GetConformer()

    for atom in mol.GetAtoms():
        idx = atom.GetIdx()
        pos = conf.GetAtomPosition(idx)
        coordinates[idx] = (atom.GetSymbol(), pos.x, pos.y, pos.z)

    return coordinates


def format_gaussian_output(atom_ids, coordinates, adjacency_list, smiles):
    """
    Outputs only the molecule name, Cartesian coordinates, and Gaussian connectivity matrix.
    """
    output = f"{smiles}\n\n"

    for idx in sorted(coordinates.keys()):
        symbol, x, y, z = coordinates[idx]
        output += f" {symbol:<2} {x:>10.6f} {y:>10.6f} {z:>10.6f}\n"

    output += "\n"

    for idx in sorted(adjacency_list.keys()):
        neighbors = adjacency_list[idx]
        if neighbors:
            output += f" {idx + 1} " + " ".join(f"{n + 1} {order:.1f}" for n, order in neighbors) + "\n"
        else:
            output += f" {idx + 1}\n"

    return output


smiles = str(input("SMILES:"))
adj_list, atom_ids = smiles_to_graph(smiles)
coordinates = smiles_to_3d_coordinates(smiles)

gaussian_output = format_gaussian_output(atom_ids, coordinates, adj_list, smiles)

formula = Chem.rdMolDescriptors.CalcMolFormula(Chem.MolFromSmiles(smiles))
with open(f"{formula}.inp", "w") as f:
    f.write(gaussian_output)

print(f"Gaussian input file saved as {formula}.inp")
