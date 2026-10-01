import { defineConfig } from 'vitepress'
import sidebar from './sidebar.json'

export default defineConfig({
  lang: 'zh-CN',
  base: '/investment-book/',
  title: '投资的世界',
  description: '写给初学者的投资通识：概念、案例与方法论',
  cleanUrls: true,
  markdown: { math: true },
  themeConfig: {
    nav: [
      { text: '阅读指南', link: '/guide' },
      { text: '目录', link: '/outline' },
      { text: '术语表', link: '/appendix/glossary' },
    ],
    sidebar,
    outline: { level: [2, 3], label: '本页内容' },
    search: { provider: 'local' },
    docFooter: { prev: '上一章', next: '下一章' },
    darkModeSwitchLabel: '外观',
    sidebarMenuLabel: '目录',
    returnToTopLabel: '回到顶部',
    footer: { message: '本书仅供学习交流，不构成任何投资建议。' },
  },
})
