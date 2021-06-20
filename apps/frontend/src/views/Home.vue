<template>
  <!--
    todo:
    - 基底コンポーネントの自動登録化
    - 分類をDB管理にする
    - ダッシュボードの改善
    - CSVインポートの改善
  -->
  <div class="home">
    <div class="flex-container">
      <div class="form-container">
        <div class="header-sub"><font class="f-normal f-moderate">明細の入力</font></div>
        <el-form
          :label-position="right"
          :model="ruleForm"
          :rules="rules"
          ref="ruleForm"
          label-width="120px"
          class="home form"
          size="small"
        >
         <!-- control the size of components in this form	string	medium / small / mini -->
          <el-row :gutter="20">
            <el-col :span="10">
              <div class="grid-content">
                <el-form-item class="form-label" label="品名" prop="itemName">
                  <el-input
                    type="text"
                    placeholder="品名を入力 (例：コンビニ、食料品、家電)"
                    v-model="ruleForm.itemName"
                    show-word-limit
                    clearable
                    :rules="rules"
                  ></el-input>
                </el-form-item>
              </div>
            </el-col>
            <el-col :span="10">
              <div class="grid-content">
                <!-- <el-tooltip class="item" effect="light" content="半角数字で入力して下さい" placement="top-start" hide-after="1000"> -->
                  <el-form-item class="form-label" label="金額" prop="itemCost">
                      <el-input
                        type="number"
                        placeholder="金額を入力（半角数字）"
                        v-model="ruleForm.itemCost"

                        show-word-limit
                        clearable
                        :rules="rules"
                      ></el-input>
                  </el-form-item>
                <!-- </el-tooltip> -->
              </div>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="10">
              <div class="grid-content">
                <div>
                  <el-form-item class="form-label" label="日付" prop="paidOn" required>
                    <el-date-picker v-model="ruleForm.paidOn" type="date" placeholder="日付を選択"></el-date-picker>
                  </el-form-item>
                </div>
              </div>
            </el-col>
            <el-col :span="10">
              <div class="grid-content">
                <el-form-item class="form-label" label="部類" prop="categoryId" required>
                  <el-select class="el-select-category" v-model="ruleForm.categoryId" placeholder="部類を選択">
                    <el-option
                      v-for="item in categorise"
                      :key="item.categoryId"
                      :label="item.value"
                      :value="item.categoryId"
                      >
                      <span style="float: left; color: #8492a6; font-size: 13px" >{{ item.value }}</span>
                      <span style="float: right">
                        <font-awesome-icon :icon="[item.iconType, item.icon]" />
                      </span>
                    </el-option>
                  </el-select>
                </el-form-item>
              </div>
            </el-col>
          </el-row>

          <el-form-item>
            <el-button class="form-button" icon="el-icon-circle-plus" @click="submitForm('ruleForm')">登録</el-button>
            <el-button class="form-button" icon="el-icon-circle-close" @click="resetForm('ruleForm')">リセット</el-button>
          </el-form-item>
        </el-form>
      </div>
      <div class="table-container">
        <div class="header-sub"><font class="f-normal f-moderate">明細の一覧</font></div>
        <el-table
          height="450px"
          :default-sort = "{prop: 'paid_on', order: 'descending'}"
          :data="rows.filter(data => !search || data.item_name.toLowerCase().includes(search.toLowerCase()))"
          style="width: 100%">
          <el-table-column
            sortable
            label="日付"
            prop="paid_on">
          </el-table-column>
          <el-table-column
            label="品名"
            prop="item_name">
          </el-table-column>
          <el-table-column
            sortable
            label="部類"
            prop="category_id"
             :formatter="categoryFormatter">
          </el-table-column>
          <el-table-column
            sortable
            label="金額"
            prop="item_cost"
            :formatter="currencyFormatter">
          </el-table-column>
          <el-table-column
            align="right">
            <!-- eslint raises error "'props' is defined but never used"  -->
            <!-- below solusion                                           -->
            <!-- https://github.com/vuejs/eslint-plugin-vue/issues/781    -->
            <template slot="header" slot-scope="{}">
              <el-input
                v-model="search"
                prefix-icon="el-icon-search"
                size="mini"
                placeholder="検索 (例：日付、品名)"/>
              <!-- Date picker below                                                 -->
              <!-- https://element.eleme.io/#/en-US/component/date-picker#datepicker -->
              <div class="date-picker-wrap">
                <el-date-picker
                  v-model="search"
                  size="mini"
                  type="month"
                  placeholder="月を選択">
                </el-date-picker>
              </div>
            </template>
            <template slot-scope="scope">
              <button @click="deleteItem(scope.$index, scope.row)" type="button" class="el-button el-button--danger is-circle">
                <i class="el-icon-delete"></i></button>
            </template>
          </el-table-column>
        </el-table>
        <div class="table-footer">
          <span class="label">合計金額：</span>
          <font class="f-normal f-moderate">
            {{ this.currencyFormatterSingle(rows.reduce((sum, value) => { return sum + value.item_cost; }, 0)) }}
          </font>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import moment from 'moment'
const axios = require('axios').create()
export default {
  computed: {
    totalitem_costs: function() {
      /* eslint-disable */
      return this.rows.reduce(
        sum,
        value => {
          /* eslint-disable */
          return sum + value.item_cost
        },
        0
      )
    }
  },
  name: 'home',
  data() {
    return {
      // todo: Manege in db.
      categorise: [
        { iconType: 'fas' ,icon: 'shopping-basket' , value: '食費' , categoryId: '1' , },
        { iconType: 'fas' ,icon: 'hamburger' , value: '外食' , categoryId: '2' , },
        { iconType: 'fas' ,icon: 'coffee' , value: 'お昼' , categoryId: '3' , },
        { iconType: 'fas' ,icon: 'film' , value: '映画' , categoryId: '4' , },
        { iconType: 'fas' ,icon: 'credit-card' , value: 'カード返済 ' , categoryId: '5' , },
        { iconType: 'fas' ,icon: 'shopping-cart' , value: '買い物 ' , categoryId: '6' , },
        { iconType: 'fas' ,icon: 'tint' , value: '水道' , categoryId: '7' , },
        { iconType: 'fas' ,icon: 'burn' , value: 'ガス' , categoryId: '8' , },
        { iconType: 'fas' ,icon: 'plug' , value: '電気' , categoryId: '9' , },
        { iconType: 'fas' ,icon: 'globe' , value: 'インターネット' , categoryId: '10' , },
        { iconType: 'fab' ,icon: 'apple' , value: 'WEBサービス' , categoryId: '11' , },
        { iconType: 'fas' ,icon: 'mobile-alt' , value: '携帯電話 ' , categoryId: '12' , },
        { iconType: 'fas' ,icon: 'cash-register' , value: 'コンビニ' , categoryId: '13' , },
        { iconType: 'fas' ,icon: 'graduation-cap' , value: '学生ローン' , categoryId: '14' , },
        { iconType: 'fas' ,icon: 'toilet-paper' , value: '消耗品' , categoryId: '15' , },
        { iconType: 'fas' ,icon: 'subway' , value: '電車' , categoryId: '16' , },
        { iconType: 'fas' ,icon: 'bus-alt' , value: 'バス' , categoryId: '17' , },
        { iconType: 'fas' ,icon: 'taxi' , value: 'タクシー' , categoryId: '18' , },
        { iconType: 'fas' ,icon: 'gift' , value: 'おみやげ' , categoryId: '19' , },
        { iconType: 'fas' ,icon: 'dumbbell' , value: 'スポーツクラブ' , categoryId: '20' , },
        { iconType: 'fas' ,icon: 'play-circle' , value: '音楽' , categoryId: '21' , },
        { iconType: 'fas' ,icon: 'cut' , value: '美容院' , categoryId: '22' , },
        { iconType: 'fas' ,icon: 'book-open' , value: '本' , categoryId: '23' , },
        { iconType: 'fas' ,icon: 'icons' , value: '趣味' , categoryId: '24' , },
        // { iconType: 'fas' ,icon: 'sercle' , value: '__' , categoryId: '25' , },
        { iconType: 'fas' ,icon: 'tshirt' , value: '衣類' , categoryId: '26' , },
        { iconType: 'fas' ,icon: 'question' , value: 'その他' , categoryId: '27' , },
      ],
      value: '',
      value1: '',
      value2: '',
      search: '',
      rules: {
        itemName: [
          {
            required: true,
            message: 'このフィールドは入力必須です。',
            trigger: 'blur'
          },
          {
            min: 1,
            max: 15,
            message: '1~15文字で入力してください',
            trigger: 'blur'
          }
        ],
        itemCost: [
          {
            required: true,
            message: 'このフィールドは入力必須です。',
            trigger: 'blur'
          },
          {
            min: 1,
            max: 15,
            message: '1~15文字で入力してください。',
            trigger: 'blur'
          }
        ],
        paidOn: [
          {
            required: true,
            message: 'このフィールドは入力必須です。',
            trigger: ['change','blur']
          }
        ],
        categoryId: [
          {
            required: true,
            message: 'このフィールドは入力必須です。',
            trigger: 'change'
          }
        ]
      },
      ruleForm: {
        itemName: '',
        itemCost: '',
        categoryId: '',
        paidOn: Date.now(),
      },
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now()
        }
      },
      rows: [
        // {
        //   id: 10,
        //   item_name: 'foo',
        //   item_cost: 900,
        //   category_id: '2',
        //   paid_on: '2020-07-12'
        // },
        // {
        //   id: 11,
        //   item_name: 'bar',
        //   item_cost: 50000000,
        //   category_id: '2',
        //   paid_on: '2020-07-13'
        // }
      ]
    }
  },
  mounted() {
    this.refreshTable()
  },
  methods: {
    deleteItem: async function(index,row) {
      const params = new URLSearchParams()
      params.append('item_id',row.id)
      axios.delete('api/list',{data:params}).then(respose => {
        this.refreshTable()})
    },
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          const params = new URLSearchParams()
          params.append('item_name', this.ruleForm.itemName)
          params.append('item_cost', this.ruleForm.itemCost)
          params.append('category_id', this.ruleForm.categoryId)
          params.append('paid_on',moment(this.ruleForm.paidOn).format('YYYY-MM-DD'))
          axios.post('api/list', params).then(respose => {
            this.refreshTable()
            return respose
          })
          this.resetForm('ruleForm')
        } else {
          return false
        }
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
    /* eslint-disable */
    categoryFormatter: function(value) {
      switch (value.category_id) {
        case '1': return '食費';
        case '2': return '外食';
        case '3': return 'お昼';
        case '4': return '映画';
        case '5': return 'カード返済';
        case '6': return '買い物';
        case '7': return '水道';
        case '8': return 'ガス';
        case '9': return '電気';
        case '10': return 'インターネット';
        case '11': return 'WEBサービス';
        case '12': return '携帯電話';
        case '13': return 'コンビニ';
        case '14': return '学生ローン';
        case '15': return '消耗品';
        case '16': return '電車';
        case '17': return 'バス';
        case '18': return 'タクシー';
        case '19': return 'おみやげ';
        case '20': return 'スポーツクラブ';
        case '21': return '音楽';
        case '22': return '美容院';
        case '23': return '本';
        case '24': return '趣味';
        // case '25': return '__';
        case '26': return '衣類';
        case '27': return 'その他';
        default: return '';
      }
    },
    /* eslint-disable */
    currencyFormatter: function(row, column) {
      return '¥ ' + row.item_cost.toLocaleString();
    },
    currencyFormatterSingle: function(value) {
      return '¥ ' + value.toLocaleString();
    },
    refreshTable: async function() {
      // const params = new URLSearchParams()
      // params.append('item_name', this.ruleForm.itemName)
      const response = await axios.get('/api/list')
      this.rows = response.data
    }
  }
}
</script>

<style lang="scss">
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
* {
  margin: 0px;
  padding: 0px;
}

.flex-container {
  display: flex;
  flex-direction: column;
  background-color:#f1f3f4;
  // padding-bottom: 140px;
  padding: 0px 120px 120px 120px;
}

.form-container {
  // padding: 25px 0 10px;
  margin: 25px;
  // background-color:white;
}
.header-sub {
  padding: 20px;
  margin-bottom: 1px;
  background-color:#fafafa;
}

.el-form {
  padding-top: 25px;
  padding-bottom: 25px;
  background-color:white;
}

.el-form-item--small .el-form-item__error {
  font-weight: normal;
}
.el-form-item {
  margin-bottom: 0px;
}

.el-form-item--small.el-form-item {
  margin-bottom: 0px;
}

.table-container {
  flex: auto;
  margin: 5px 25px;
}

.el-date-editor.el-input,
.el-date-editor.el-input__inner {
  width: 280px;
}

.table-footer {
  padding: 20px 0;
  background-color: white;
}

.table-footer .label {
  color: #909399;
  font-weight: bold;
  padding-left: 10px
}
.el-button.is-circle {
  padding: 4px;
  margin-right: 12px;
}
.text-center {
  text-align: center;
}
.vgt-global-search__input .input__icon {
  display: none;
}
.form-button {
  width: 95px;
}

.form-label{
  font-weight: bold;

}
.el-input--mini .el-input__inner {
  margin-bottom: 3px;
}

.el-date-editor.el-input, .el-date-editor.el-input__inner {
  width: 100%;
  -webkit-box-sizing: border-box;  /*webkit系*/
  -moz-box-sizing: border-box;  /*Firefox*/
  box-sizing: border-box;
}

.el-select-category {
  width: 100%;
  -webkit-box-sizing: border-box;  /*webkit系*/
  -moz-box-sizing: border-box;  /*Firefox*/
  box-sizing: border-box;
}

font.f-normal {
  font-size: 14px;
}

font.f-moderate {
  color: #909399
}

// spin button off
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="number"] {
  -moz-appearance:textfield;
}
</style>
