import TestCaseList from '@/components/TestEdit/TestCaseList'
import TestCaseEditForm from '@/components/TestEdit/TestCaseEditForm'

export default {
  name: 'TestEdit',

  components: {
    'test-case-list': TestCaseList,
    'test-case-edit-form': TestCaseEditForm
  },

  data () {
    return {
      selectTestCaseName: null
    }
  },

  methods: {
    handleClickTestCase(testCaseName) {
      this.selectTestCaseName = testCaseName
    }
  }
}
