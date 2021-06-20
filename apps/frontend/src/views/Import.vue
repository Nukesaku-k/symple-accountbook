<template>
  <section>
    <div class="flex-container">
      <el-upload
        class="upload-demo"
        drag
        action=""
        :on-change="handleAdd"
        :on-remove="deleteDropFile"
        :file-list="fileList"
        :auto-upload="false"
        :limit="1"
        :multiple="false">
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
        <div class="el-upload__tip" slot="tip">CSV files with a size less than 500kb</div>
      </el-upload>
      <div v-if="fileList.length > 0" class="block">
          <el-button class="form-button form-button-import" icon="el-icon-circle-plus" @click="submitForm(rows)">登録</el-button>
      </div>
     <div class="table-container">
        <el-table
          height="450px"
          :default-sort = "{prop: 'paid_on', order: 'descending'}"
          :data="rows.filter(data => !search || data.item_name.toLowerCase().includes(search.toLowerCase()))"
          style="width: 100%">
          <el-table-column
            sortable
            label="Date"
            prop="paid_on">
          </el-table-column>
          <el-table-column
            label="Item"
            prop="item_name">
          </el-table-column>
          <el-table-column
            sortable
            label="Category"
            prop="category_id"
             :formatter="categoryFormatter">
          </el-table-column>
          <el-table-column
            sortable
            label="Cost"
            prop="item_cost"
            :formatter="currencyFormatter">
          </el-table-column>
          <el-table-column
            align="right">
            <template slot="header" slot-scope="{}">
              <el-input 
                v-model="search"
                prefix-icon="el-icon-search"
                size="mini"
                placeholder="Search items"/>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </section>
</template>

<script>
import moment from 'moment'
const axios = require('axios').create()

export default {
  name: 'UploadForm',
  data () {
    return {
      fileList: [],
      rows: [],
    }
  },
  methods: {
    // アップロードしたファイル削除用
    /* eslint-disable */
    deleteDropFile: function() {
      this.fileList = [],
      this.rows = []
    },
    uploadedData: function() {
      this.rows = []
      const csvfile = this.fileList[0].raw
      const reader = new FileReader()

      const loadCSV = () => {
        const lines = reader.result.split('\n')
        lines.shift() // csvファイルの先頭（ヘッダ）を削除

        /* eslint-disable */
        lines.forEach((element, index) => {
          const workerData = element.split(',')
          if (workerData.length !== 4) { return }
          this.rows.push(
            {
              id: index,
              paid_on: moment(workerData[0]).format('YYYY-MM-DD'),
              item_name: workerData[1],
              category_id: workerData[2],
              item_cost: workerData[3],
            }
          )
        })
      }
      reader.onload = loadCSV
      reader.readAsText(csvfile)
    },
    handleAdd: function(file, fileList) {
      this.fileList = fileList
      this.uploadedData()
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
        case '25': return '着物';
        case '26': return '衣類';
        case '27': return 'その他';
        default: return '';
      }
    },
    /* eslint-disable */
    currencyFormatter: function(row, column) {
      return '¥ ' + row.item_cost.toLocaleString();    
    },
    submitForm: function(rows) {
      const params = new URLSearchParams()
      // todo:request at onece.
      rows.forEach((element,index,rows) => {
        params.append('item_name', rows[index].item_name)
        params.append('item_cost', rows[index].item_cost)
        params.append('category_id', rows[index].category_id)
        params.append('paid_on',moment(rows[index].paid_on).format('YYYY-MM-DD'))
        axios.post('api/list', params).then(respose => {
          return respose
        })
      })
      alert('Submited!')
      this.deleteDropFile()
    }
  }
}
</script>
<style>
.upload-demo {
  margin:  25px auto;
}
.form-button-import {
  margin-left: 25px;
}
</style>