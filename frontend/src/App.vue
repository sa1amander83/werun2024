<script>
import {RouterLink, RouterView} from 'vue-router'
// import 'bootstrap/dist/css/bootstrap.min.css'
// import 'bootstrap-vue/css/bootstrap-vue.css'
// import {BootstrapVue} from 'bootstrap-vue'
// import Vue from 'vue'
// import axios from  'axios'
// import VueAxios from "vue-axios";
import './assets/js/bootstrap.min.js'
import './assets/css/bootstrap.min.css'

export default {
  data() {
    return {}
  },
  compatConfig: {
    MODE: 3,
  },

}

</script>

<template>

  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">


  </head>

    <div class="wrapper">


      <header class=" flex justify-between items-center p-6">
        <div class="flex items-center gap-2">
          <svg class="h-10 text-blue-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
            <path fill-rule="evenodd"
                  d="M5.166 2.621v.858c-1.035.148-2.059.33-3.071.543a.75.75 0 00-.584.859 6.753 6.753 0 006.138 5.6 6.73 6.73 0 002.743 1.346A6.707 6.707 0 019.279 15H8.54c-1.036 0-1.875.84-1.875 1.875V19.5h-.75a2.25 2.25 0 00-2.25 2.25c0 .414.336.75.75.75h15a.75.75 0 00.75-.75 2.25 2.25 0 00-2.25-2.25h-.75v-2.625c0-1.036-.84-1.875-1.875-1.875h-.739a6.706 6.706 0 01-1.112-3.173 6.73 6.73 0 002.743-1.347 6.753 6.753 0 006.139-5.6.75.75 0 00-.585-.858 47.077 47.077 0 00-3.07-.543V2.62a.75.75 0 00-.658-.744 49.22 49.22 0 00-6.093-.377c-2.063 0-4.096.128-6.093.377a.75.75 0 00-.657.744zm0 2.629c0 1.196.312 2.32.857 3.294A5.266 5.266 0 013.16 5.337a45.6 45.6 0 012.006-.343v.256zm13.5 0v-.256c.674.1 1.343.214 2.006.343a5.265 5.265 0 01-2.863 3.207 6.72 6.72 0 00.857-3.294z"
                  clip-rule="evenodd"/>
          </svg>

          <span class="text-xl font-black">МыЗабег2024</span>

        </div>
          </header>
        <div>

          <a class="rounded-end-5 bg-blue-600 py-2 px-4 text-white font-semibold shadow-lg hover:shadow-xl focus:shadow-xl hover:bg-blue-700 focus:outline-none focus: right-2 focus:ring-blue-500 focus:ring-offset-2 transition duration-150 ease-in-out"
             href="#">Sign In</a>
        </div>

      <div class="flex">
        <div class="col-3">
          left
        </div>
        <div>
          center
        </div>
        <div class="flex flex-1">
          right
        </div>
      </div>


      <nav>
        <RouterLink to="/">Главная</RouterLink>
        <RouterLink to="/registration">Регистрация</RouterLink>
        <RouterLink to="/login">Войти</RouterLink>
      </nav>
    </div>


  <RouterView/>

  <body>
  </body>
</template>

<style scoped >
header {
  line-height: 1.5;
  max-height: 100vh;
}


nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    /*display: flex;*/
    /*place-items: center;*/
    /*padding-right: calc(var(--section-gap) / 2);*/
  }


  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
