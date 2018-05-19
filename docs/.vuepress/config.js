module.exports = {
  title: 'Interview Book',
  description: 'Just read it',
  head: [
    ['link', { rel: 'icon', href: '~@imgs/bone.png' }],
  ],
  base: '/Interview-Book/',
  configureWebpack: {
    resolve: {
      alias: {
        '@imgs': 'assets/imgs'
      }
    }
  },
  themeConfig: {
    nav: [
      { text: 'Guide', link: '/guide/' },
    ],
    sidebar: {
      '/guide/': [
        {
          title: 'Guide',
          collapsable: false,
          children: [
            '',
            'entry',
            'basic',
            'advanced',
            'framework',
            'architecture',
            'team',
            'foundation'
          ]
        }
      ]
    },
    repo: 'https://github.com/Liyuk/Interview-Book',
    repoLabel: 'Github',
    // 默认是 false, 设置为 true 来启用
    editLinks: true,
    // 默认为 "Edit this page"
    editLinkText: '帮助我们改善此页面！'
  }
}