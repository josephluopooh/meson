

mytarget = custom_target('depfile',
  output : 'dep.dat',
  depfile : 'dep.dat.d',
  command : [find_program('dep.py'), meson.current_source_dir(), '@DEPFILE@', '@OUTPUT@'],
)

# A depfile may also be listed as an output of the same custom target.
custom_target('depfile-output',
  output : ['dep-with-output.dat', 'dep-with-output.d'],
  depfile : 'dep-with-output.d',
  command : [find_program('dep.py'), meson.current_source_dir(), '@DEPFILE@', '@OUTPUT0@'],
  build_by_default : true,
)
