import { getTestCaseList, getTestCase } from '@/common/api'

export default {
  name: 'TestCaseList',

  data () {
    return {
      testcaseList: []
    }
  },

  async mounted () {
    const response = await getTestCaseList()
    this.testcaseList = response.testcaseList
  },

  methods: {
    handleClickTestCase(testCaseName) {
      this.$emit('click-test-case', testCaseName)
    }
  }
}
