project('extra-files-dependency', 'c', meson_version: '>=1.2.0')

foo_dep = subproject('foo').get_variable('foo_dep')
wrapper_dep = declare_dependency(
  dependencies: foo_dep,
  extra_files: files('wrapper.txt'),
)

executable(
  'example',
  'main.c',
  dependencies: [wrapper_dep, foo_dep],
  extra_files: files('direct.txt'),
)
