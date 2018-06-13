module.exports = {
  title: 'Interview Book',
  description: '前端面试题以及前端知识点梳理',
  dest: 'dist',
  base: '/Interview-Book/',
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
    repo: 'https://github.com/Mountain-Buzhou/Interview-Book',
    repoLabel: 'Github',
    docsDir: 'docs',
    // 假如文档放在一个特定的分支下：
    docsBranch: 'vuepress',
    // 默认是 false, 设置为 true 来启用
    editLinks: true,
    // 默认为 "Edit this page"
    editLinkText: '帮助我们改善此页面！'
  }
}