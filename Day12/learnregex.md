比较有趣的正则表达式
分组的理解
描述一个正确的IP地址：((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)

我是这么理解的
2[0-4]\d 即代表200-249
25[0-5] 代表250-255
[01]?\d\d? 代表0或者1开头，出现零次或者1次，\d代表0-9任意数字，\d？代表0-9出现0次或者1次（）

三个条件组合用 | 来分隔，组成 01-255的IP段，并且带有.尾巴（\.）

{3} 即代表上述3个条件重复判断3次，
xxx.xxx.xxx.

后半段(2[0-4]\d|25[0-5]|[01]?\d\d?)即IP段第四位，判断条件跟上述一致，只是少了\.这个尾巴