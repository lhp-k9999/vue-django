<template>
    <div class="login">
        <!--        vue的组件是如何使用：-->
        <!--&lt;!&ndash;        1. 创建vue组件&ndash;&gt;components/header.vue-->
        <!--                    2. 在父组件里面导入组件的路径-->
        <!--                    3. 在父组件里面的components进行注册-->
        <!--                    4. 然后在父组件里面的html部分按照定义的key当做标签来使用-->
        <header-component></header-component>
        <div class="login-context">
            <h2>账号登录</h2>

            <!--            rules 校验规则 ，model绑定数据，子数据el-form-item的 v-model是绑定数据的属性-->

            <!--            ref唯一id找出元素对象，vue使用ref，js使用id-->
            <!--             1、先在元素里定义ref为XXX，然后在vue使用 this.$refs.XXX 就可以获取元素对象-->

            <el-form label-position="left" :model="loginForm" :rules="rules" ref="loginFormRef" label-width="50px" class="demo-ruleForm">
                <el-form-item label="用户名" prop="name">
                    <el-input v-model="loginForm.name" placeholder="请输入用户名"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="passWord">
                    <el-input v-model="loginForm.passWord" show-password placeholder="请输入密码"></el-input>
                </el-form-item>
            </el-form>

            <div class="login-button-class">
                <el-button type="success" @click="login">登录</el-button>
                <el-button type="danger" @click="register">注册</el-button>
            </div>
        </div>
    </div>
</template>

<script>
  // 2. 在父组件里面导入组件的路径-->
  import header from '../components/header'
    export default {
        name: 'login',
      // 3.在父组件里面的components进行注册 ，header-component 作为引入名
        components: {
            "header-component": header,
        },
        props: {},
        data() {
            return {
                loginForm: {
                    name: "",
                    passWord: "",
                },
              // el-form-item 的prop写rules的属性名

                rules: {
                    name: [
                      { required: true, message: '请输入用户名!', trigger: 'blur' },
                        {min: 1, max: 30, message: '长度在 1 到 30 个字符', trigger: 'blur'}
                    ],
                    passWord: [
                      { required: true, message: '请输入用户密码!', trigger: 'blur' },
                        {min: 1, max: 30, message: '长度在 1 到 30 个字符', trigger: 'blur'}
                    ],
                },

        }
        },
        methods: {
            login() {
              // Vue3.0 console.log()语法报错 只需要改成window.console.log() 即可解决
              window.console.log(this.$refs.loginFormRef)
              this.$refs.loginFormRef.validate((valid) => {
                    if (valid) { // 代表校验通过
                      alert('校验通过')
                    } else {  //校验失败
                      alert('校验失败')
                      return false
                    }
                });
              // this.validForm();
            },
            register() {
                this.$refs.loginFormRef.validate((valid) => {
                    if (valid) { // 代表校验通过
                    } else {  //校验失败
                        return false;
                    }
                });
            },
          // 初级的表单验证
          // validForm(){
          //   if ("" == this.loginForm.name){
          //     alert("用户名不能为空")
          //     return
          //   }
          //   if ("" == this.loginForm.passWord){
          //     alert("密码不能为空")
          //     return
          //   }
          // }
        },
        created() {

        }
    }
</script>

<style scoped>

    .login-context {
        width: 400px;
        margin-left: auto;
        margin-right: auto;
        border-radius: 2px;
        border: 1px solid #a0b1c4;
        margin-top: 50px;
        padding: 10px 30px;
    }

    .login-button-class {
        display: flex;
        justify-content: space-between;
    }


</style>