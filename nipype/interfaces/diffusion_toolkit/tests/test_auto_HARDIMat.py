# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..odf import HARDIMat


def test_HARDIMat_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bvals=dict(mandatory=True,
    ),
    bvecs=dict(argstr='%s',
    mandatory=True,
    position=1,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    image_info=dict(argstr='-info %s',
    ),
    image_orientation_vectors=dict(argstr='-iop %f',
    ),
    oblique_correction=dict(argstr='-oc',
    ),
    odf_file=dict(argstr='-odf %s',
    ),
    order=dict(argstr='-order %s',
    ),
    out_file=dict(argstr='%s',
    position=2,
    usedefault=True,
    ),
    reference_file=dict(argstr='-ref %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = HARDIMat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_HARDIMat_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = HARDIMat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value