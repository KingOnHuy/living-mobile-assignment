<template lang="">
    <div>
        <el-row>
            <el-col :span="10"> <h2> Store </h2></el-col>
            <el-col :span="10" :offset="2">
                <el-button type="primary" round>+ Add New Store</el-button>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="10" :offset="2">
                <el-table
                :data="tableData"
                style="width: 100%">
                <el-table-column
                    prop="date"
                    label="Date"
                    width="180">
                </el-table-column>
                <el-table-column
                    prop="name"
                    label="Name"
                    width="180">
                </el-table-column>
                <el-table-column
                    prop="address"
                    label="Address">
                </el-table-column>
                </el-table>
            </el-col>
        </el-row>
    </div>
</template>
<script>
export default {
    data() {
        return {
          tableData: [{
            date: '2016-05-03',
            name: 'Tom',
            address: 'No. 189, Grove St, Los Angeles'
          }, {
            date: '2016-05-02',
            name: 'Tom',
            address: 'No. 189, Grove St, Los Angeles'
          }, {
            date: '2016-05-04',
            name: 'Tom',
            address: 'No. 189, Grove St, Los Angeles'
          }, {
            date: '2016-05-01',
            name: 'Tom',
            address: 'No. 189, Grove St, Los Angeles'
          }]
        }
      }
}
</script>
<style lang="">
    
</style>