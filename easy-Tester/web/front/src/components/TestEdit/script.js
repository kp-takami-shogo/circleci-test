export default {
  name: 'TestEdit',

  data () {
    return {
      project: '',
      branch: '',
      test: '',
      testcase: ''
    }
  },

  methods: {
    handleClickBranchList (project) {
      this.project = project
    },

    handleClickTestList (branch) {
      this.branch = branch
    },

    handleClickTestCaseList (test) {
      this.test = test
    },

    handleClickProcessList (testcase) {
      this.testcase = testcase
    }
  }
}
