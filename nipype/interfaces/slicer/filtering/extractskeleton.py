"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os
from nipype.interfaces.slicer.base import SlicerCommandLine


class ExtractSkeletonInputSpec(CommandLineInputSpec):
    OutputImageFileName = traits.Either(traits.Bool, File(), position=-1, hash_files=False, desc="Skeleton of the input image", argstr="%s")
    type = traits.Enum("1D", "2D", desc="Type of skeleton to create", argstr="--type %s")
    dontPrune = traits.Bool(desc="Return the full skeleton, not just the maximal skeleton", argstr="--dontPrune ")
    numPoints = traits.Int(desc="Number of points used to represent the skeleton", argstr="--numPoints %d")
    pointsFile = traits.Str(desc="Name of the file to store the coordinates of the central (1D) skeleton points", argstr="--pointsFile %s")


class ExtractSkeletonOutputSpec(TraitedSpec):
    OutputImageFileName = File(position=-1, desc="Skeleton of the input image", exists=True)


class ExtractSkeleton(SlicerCommandLine):
    """title: Extract Skeleton

category: Filtering

description: Extract the skeleton of a binary object.  The skeleton can be limited to being a 1D curve or allowed to be a full 2D manifold.  The branches of the skeleton can be pruned so that only the maximal center skeleton is returned.

version: 0.1.0.$Revision: 2104 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/ExtractSkeleton

contributor: Pierre Seroul (UNC), Martin Styner (UNC), Guido Gerig (UNC), Stephen Aylward (Kitware)

acknowledgements: The original implementation of this method was provided by ETH Zurich, Image Analysis Laboratory of Profs Olaf Kuebler, Gabor Szekely and Guido Gerig.  Martin Styner at UNC, Chapel Hill made enhancements.  Wrapping for Slicer was provided by Pierre Seroul and Stephen Aylward at Kitware, Inc.

"""

    input_spec = ExtractSkeletonInputSpec
    output_spec = ExtractSkeletonOutputSpec
    _cmd = "/home/raid3/gorgolewski/software/slicer/Slicer --launch ExtractSkeleton "
    _outputs_filenames = {'OutputImageFileName':'OutputImageFileName.nii'}