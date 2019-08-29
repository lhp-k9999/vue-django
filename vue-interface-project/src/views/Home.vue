<template>
    <div class="home">
        <header-component></header-component>
    </div>
</template>

<script>
    import {getUserInfoRequest} from "../requests/user";
    import header from "../components/header"

    export default {
        name: 'home',
        components: {
            "header-component": header,
        },
        methods: {
            tellIfUserIsLogin() {
                // 首页需要有判断用户是否已经登录的逻辑：
                // 用户如果已经登录，则不作任何事情； 如果用户没有登录，则进行跳转到登录页面（this.$router.push("/login")）
                getUserInfoRequest().then(data => {
                    if (false === data.data.success) {
                        this.$router.push("/login");
                        // window.location("/login")
                    }
                }).catch(data => {
                    console.log(data);
                })
            },
        },
        created() {
            this.tellIfUserIsLogin();
        },
    }
</script>

<style scoped>

</style>
