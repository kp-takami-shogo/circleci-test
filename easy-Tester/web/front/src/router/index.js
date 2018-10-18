import Vue from 'vue'
import Router from 'vue-router'
import TestEdit from '@/components/TestEdit'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/test-edit',
      name: 'TestEdit',
      component: TestEdit
    }
  ]
})
