<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Регистрация участника</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Номер участника</label>
            <div class="control">
              <input type="number" name="runner" class="input" v-model="username">
            </div>
          </div>

          <div class="field">
            <label>Пароль</label>
            <div class="control">
              <input type="password" name="password1" class="input" v-model="password1">
            </div>
          </div>

          <div class="field">
            <label>Повторите пароль</label>
            <div class="control">
              <input type="password" name="password2" class="input" v-model="password2">
            </div>
          </div>


          <div class="field">
            <label>Команда </label>
            <div class="control">
              <input type="" name="runner_team" class="input">
            </div>
          </div>

          <div class="field">
            <label>Возраст </label>
            <div class="control">
              <input type="number" name="runner_age" class="input">
            </div>
          </div>

          <div class="field">
            <label> Пол </label>
            <div class="control">
              <select v-model="selected">
                <option v-for="option in options" :value="option.value">
                  {{ option.text }}
                </option>
              </select>
            </div>
          </div>

          <div class="field">
            <label>Категория</label>
            <div class="control">

              <select>

                <option v-if="selected==='М'" v-for="option in options2" :value="option.value">
                  {{ option.text }}
                </option>
                <option v-else v-for="option in options3" :value="option.value">
                  {{ option.text }}
                </option>
              </select>
            </div>
          </div>

          <div class="field">


            <div class="control">
              <input type="checkbox" id="zabeg22" name="zabeg22" class="input" v-model="checked"/>&nbsp
              <label for="checkbox">Участник "МыZaБег 2022"  </label>
            </div>
          </div>
          <div class="field">

            <div class="control">
              <input type="checkbox" id="zabeg23" name="zabeg23" class="input">&nbsp
              <label for="checkbox">Участник "МЫЗАБЕГ 2023"</label>
            </div>
          </div>


          <div class="notification is-danger danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import {toast} from 'bulma-toast'

export default {
  name: 'SignUp',
  selected: null,
  data() {

    return {

      selected: 'М',
      options: [
        {text: 'М', value: 'М'},
        {text: 'Ж', value: 'Ж'}
      ],


      selected2: 1,
      options2: [
        {text: 'Новичок', value: 1},
        {text: 'Любитель', value: 2},
        {text: 'Профи', value: 3}
      ],
      options3: [
        {text: 'Новичок', value: 1},
        {text: 'Любитель', value: 2},
      ],


      username: '',
      password1: '',
      password2: '',
      errors: []
    };

  },

  methods: {
  submitForm() {
      this.errors = []

      if (this.username === '') {
        this.errors.push('Не введен номер участника')
      }

      if (this.password1 === '') {
        this.errors.push("Вы не ввели пароль")
      }

      if (this.password1 !== this.password2) {
        this.errors.push('Пароли не совпадают')
      }

      if (!this.errors.length) {
        // this.$store.commit('setIsLoading', true)

        const formData = {
          runner: this.username,
          password: this.password1,
          runner_team: this.runner_team,
          runner_age: this.runner_age,
          runner_category: this.runner_category,
          runner_gender: this.runner_gender,
          zabeg22:this.zabeg22,
          zabeg23:this.zabeg23
        }

             axios
          .post('http://localhost:8000/registration', formData)
          // .post(this.store.state.endpoints.obtainJWT, formData)
          .then((response) => {
            console.log(formData)
            // this.store.commit("updateToken", response.data.token);
            // get and set auth user
            const base = {
              baseURL: this.store.state.endpoints.baseUrl,
              headers: {
                // Set your Authorization to 'JWT', not Bearer!!!
                Authorization: `JWT ${this.store.state.jwt}`,
                "Content-Type": "application/json",
              },
              xhrFields: {
                withCredentials: true,
              },
            };

            const axiosInstance = axios.create(base);
            axiosInstance({
              url: "/registration/",
              method: "get",
              params: {},
            }).then((response) => {
              this.store.commit("setAuthUser", {
                authUser: response.data,
                isAuthenticated: true,
              });

              this.router.push('/login')
            });
          })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
              } else if (error.message) {
                this.errors.push('Что-то пошло не так!')
              }
            })

        // this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>