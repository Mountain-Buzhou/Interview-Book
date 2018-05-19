module.exports = {
  title: 'Interview Book',
  description: 'Just read it',
  base: '/Interview-Book/',
  themeConfig: {
    nav: [
      { text: 'Guide', link: '/guide/' },
      { text: 'Github', link: 'https://github.com/Liyuk/Interview-Book' },
    ],
    sidebar: {
      '/guide/': [
        {
          title: 'Guide',
          collapsable: false,
          children: [
            '',
            'abstract',
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
    }
  }
}