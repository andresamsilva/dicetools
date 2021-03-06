#!/usr/bin/env python3
"""
Given the filename of batch of several xyz molecules, compute the angles
between a1-a2-a3 (provided by the user) and print them in stdout.

Author: Henrique Musseli Cezar
Date: OCT/2016
"""

import argparse
import pybel
import openbabel
import os

def get_dihedrals(fname, a1, a2, a3):
  # read all the molecules from file
  for mol in pybel.readfile(os.path.splitext(fname)[1][1:], fname):
    print(mol.OBMol.GetAngle(mol.OBMol.GetAtom(a1),mol.OBMol.GetAtom(a2),mol.OBMol.GetAtom(a3)))


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Receives a file with several xyz molecules and compute the desired angle for each one of them.")
  parser.add_argument("filename", help="the file containing the molecules")
  parser.add_argument("atom1", help="number of the first atom in the angle")
  parser.add_argument("atom2", help="number of the second (central) atom in the angle")
  parser.add_argument("atom3", help="number of the third atom in the angle")
  args = parser.parse_args()

  get_dihedrals(args.filename, int(args.atom1), int(args.atom2), int(args.atom3))