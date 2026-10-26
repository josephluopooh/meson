project('pkgconfig partial dependency', 'c', version: '1.0')

pkg = import('pkgconfig')
dep = dependency('full-dependency', method: 'pkg-config')
partial = dep.partial_dependency(compile_args: true)

lib = library('partial', 'lib.c', dependencies: partial, install: true)
pkg.generate(lib)
pkg.generate(name: 'partial-public', description: 'Compile arguments only',
             version: '1.0', libraries: partial)
pkg.generate(name: 'partial-links', description: 'Link arguments only',
             version: '1.0', libraries: dep.partial_dependency(link_args: true))
pkg.generate(name: 'complete-dependency', description: 'Complete dependency',
             version: '1.0', libraries: dep)
