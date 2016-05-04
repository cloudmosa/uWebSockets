{
  'targets': [
    {
      'target_name': 'uws',
      'sources': [
        'src/uWS.cpp',
        'src/addon.cpp'
      ],
      'cflags_cc': [ '-std=c++11', '-fexceptions' ]
    },
    {
      'target_name': 'action_after_build',
      'type': 'none',
      'dependencies': [ 'uws' ],
      'actions': [
        {
          'action_name': 'move_lib',
          'inputs': [
            '<@(PRODUCT_DIR)/uws.node'
          ],
          'outputs': [
            'uws'
          ],
          'action': ['cp', '<@(PRODUCT_DIR)/uws.node', 'uws.node']
        }
      ]
    }
  ]
}
