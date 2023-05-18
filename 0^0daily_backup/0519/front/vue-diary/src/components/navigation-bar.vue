<template>
  <div id="app">
    <navigation-bar :options="navigationData"/>
  </div>
</template>

<script>
// 나중에 레이아웃 받고 참고해서 해보기
export default {
  name: 'NavBar',
  data(){
    return {
      navigationData: {
        elementId: "main-navbar",
        isUsingVueRouter: true,
        collapseButtonOpenColor: "#661c23",
        collapseButtonCloseColor: "#661c23",
        showBrandImageInMobilePopup: true,
        menuOptionsLeft: [ // 메뉴 좌측에 들어갈 항목(Array)
        {
            type: "link", // 메뉴 종류. link, spacer, button, dropdown이 있다.
            text: "영화", // 보여줄 text            
            arrowColor: "#659CC8", // 화살표 색상
            subMenuOptions: [ // 하위 메뉴 목록 (Array)
                {
                    type: "link", // 메뉴 종류. link, spacer, button, dropdown이 있다.
                    text: "개봉작", // 보여줄 text
                    path: "/newmovie",  // 클릭 시 이동 할 경로
                },
                {
                    type: "link", // 메뉴 종류. link, spacer, button, dropdown이 있다.
                    text: "부산", // 보여줄 text
                    path: "/seoul",  // 클릭 시 이동 할 경로
                }
            ]   
        }                        
    ]   

      }
    }
  }
}
</script>