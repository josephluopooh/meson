project('fuzzer sanitizer', 'c', 'cpp')

code = import('fs').read('fuzzer.c')
foreach lang : ['c', 'cpp']
  compiler = meson.get_compiler(lang)
  if compiler.get_id() not in ['clang', 'apple-clang']
    error('MESON_SKIP_TEST: requires Clang libFuzzer')
  endif
  if not compiler.links(code, args: ['-fsanitize=fuzzer'], name: 'libFuzzer runtime')
    error('MESON_SKIP_TEST: libFuzzer runtime not available')
  endif
  exe = executable('fuzzer-' + lang, 'fuzzer.' + lang)
  test('fuzzer-' + lang, exe, args: ['-runs=1'])
endforeach
