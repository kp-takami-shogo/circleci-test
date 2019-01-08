import { getTestCase } from '@/common/api'

export default {
  name: 'TestCaseEditForm',

  props: {
    selectTestCaseName: {
      type: String,
      default: () => {
        return null
      }
    }
  },

  data () {
    return {
      testCase: []
    }
  },

  watch: {
    selectTestCaseName: async function () {
      if (!this.selectTestCaseName) return false

      const response = await getTestCase(this.selectTestCaseName)
      this.testCase = response.testcase
    }
  },

  methods: {
  }
}
