!function(){
    //初始化swiper
    var view = document.querySelector('#mySlides')
    var mySwiper = new Swiper(view.querySelector('.swiper-container'), {
        loop: true, // 循环模式选项
        // 如果需要分页器
        pagination: {
            el: '.swiper-pagination',
        },
        // 如果需要前进后退按钮
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    })
}.call()  

!function(){
    //页面点击导航栏滚动
    setTimeout(function () {
        sw.classList.remove('active')
    }, 1000)
    //添加offset类
    let specialTags = document.querySelectorAll('[data-x]')
    for (let i = 0; i < specialTags.length; i++) {
        specialTags[i].classList.add('offset')
    }
    setTimeout(function () {
        yyy()
    }, 1000)

    //滑动到每个页面，对应的标签高亮
    window.onscroll = function (xxx) {
        if (window.scrollY > 0) {
            topNavbar.classList.add('sticky')
        } else {
            topNavbar.classList.remove('sticky')
        }
        yyy()
    }
    //标签高亮函数
    function yyy() {
        let specialTags = document.querySelectorAll('[data-x]')
        let minindex = 0
        for (let i = 0; i < specialTags.length; i++) {
            if (Math.abs(specialTags[i].offsetTop - window.scrollY) < Math.abs(specialTags[minindex].offsetTop - window.scrollY)) {
                minindex = i
            }
        }
        //minindex就是离窗口顶部最近的元素
        specialTags[minindex].classList.remove('offset')
        let id = specialTags[minindex].id
        let a = document.querySelector('a[href="#' + id + '"]')
        let li = a.parentNode
        let child = li.parentNode.children
        for (let i = 0; i < child.length; i++) {
            child[i].classList.remove('highlight')
        }
        li.classList.add('highlight')
    }
}.call()



!function(){
    //缓动动画
    var view =document.querySelector('nav.menu')
    let liTags = view.querySelectorAll('nav.menu > ul > li')
    function animate(time) {
        requestAnimationFrame(animate);
        TWEEN.update(time);
    }
    requestAnimationFrame(animate);

    for (let i = 0; i < liTags.length; i++) {
        liTags[i].onmouseenter = function (x) {
            x.currentTarget.classList.add('active')

        }
        liTags[i].onmouseleave = function (x) {
            x.currentTarget.classList.remove('active')
        }
    }
    let aTags = document.querySelectorAll('nav.menu > ul >li > a')
    for (let i = 0; i < aTags.length; i++) {
        aTags[i].onclick = function (x) {
            x.preventDefault()   //阻止浏览器滚动默认动作
            let a = x.currentTarget
            let href = a.getAttribute('href')// 不带http协议，a.href带http协议   #siteAbout
            let element = document.querySelector(href)
            let top = element.offsetTop   //获取距离顶部长度

            let currentTop = window.scrollY
            let targetTop = top - 65
            let s = targetTop - currentTop       //路程
            var coords = { y: currentTop };       //起始位置
            var t = Math.abs((s / 100) * 500)       //时间
            if (t > 3000) { t = 1500 }
            var tween = new TWEEN.Tween(coords)     //起始位置
                .to({ y: targetTop }, t)        //结束位置和时间
                .easing(TWEEN.Easing.Quadratic.InOut)       //缓动类型（先慢后快再慢）
                .onUpdate(function () {
                    window.scrollTo(0, coords.y)     //更新界面
                })
                .start();       //开始缓动
        }
    }
}.call()

