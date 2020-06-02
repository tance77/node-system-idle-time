{
  "targets": [{
    "target_name": "system_idle_time",
    "sources": [
      "src/module.cc"
    ],
    "include_dirs": [
      "<!(node -e \"require('nan')\")"
    ],
    "conditions": [
      ['OS=="mac"', {
        "defines": [
          "OS=1"
        ],
        "sources": [
          "src/mac/idle.cc"
        ],
        "xcode_settings": {
          'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
          'CLANG_CXX_LIBRARY': 'libc++',
          'GCC_ENABLE_CPP_EXCEPTIONS': 'NO',
          'MACOSX_DEPLOYMENT_TARGET': '10.7',
          "OTHER_CPLUSPLUSFLAGS": ["-std=c++11", "-stdlib=libc++"],
        "OTHER_LDFLAGS": ["-framework CoreFoundation -framework IOKit"]
        }
      }],
        ['OS!="win"', {
            'cflags_cc+': [
              '-std=c++0x'
        ]
      }],
      ['OS=="win"', {
        "defines": [
          "OS=2"
        ],
        "sources": [
          "src/win/idle.cc"
        ],
         'msvs_settings': {
            'VCCLCompilerTool': {
              'AdditionalOptions': [
                # disable Thread-Safe "Magic" for local static variables
                '/Zc:threadSafeInit-',
              ],
            },
          },
     }],
     ['OS=="linux"', {
       "defines": [
        "OS=3"
      ],
      'variables': {
	'pkg-config': 'pkg-config'
      },
      "sources": [
        "src/linux/idle.cc"
      ],
      'direct_dependent_settings': {
        'cflags': [
          '<!@(<(pkg-config) --cflags x11 xext xscrnsaver)',
        ],
      },
      'link_settings': {
        'ldflags': [
          '<!@(<(pkg-config) --libs-only-other --libs-only-L x11 xext xscrnsaver)',
        ],
        'libraries': [
          '<!@(<(pkg-config) --libs-only-l x11 xext xscrnsaver)',
        ],
      },
     }]
    ]
  }]
}
