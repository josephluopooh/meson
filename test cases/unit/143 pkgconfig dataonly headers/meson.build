project('dataonly headers', version: '1.0')

pkg = import('pkgconfig')
pkg.generate(
  name: 'dataonly-headers',
  description: 'Architecture-independent headers and data',
  dataonly: true,
  subdirs: 'dataonly-headers',
  extra_cflags: '-DDATAONLY_HEADERS=1',
)
pkg.generate(
  name: 'dataonly-plain',
  description: 'Only architecture-independent data',
  dataonly: true,
)

python = find_program('python3', 'python')
run_command(
  python, files('check.py'),
  meson.current_build_dir() / 'meson-private',
  check: true,
)
