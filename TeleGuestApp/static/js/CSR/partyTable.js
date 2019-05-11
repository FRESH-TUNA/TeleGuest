var tableHeaderComponent = {
    template:
    `
    <thead class="thead-light">
                <tr>
                    <th>콘서트이름</th>
                    <th>가수</th>
                    <th>콘서트날짜</th>
                    <th>글쓴이이메일</th>
                    <th>게시날짜</th>
                    <th>수정</th>
                    <th>삭제</th>
                    <th>상세정보</th>
                </tr>
    </thead>
    `
};

var teleguestTableHeader = new Vue({
    delimiters: ["[[","]]"],
    el: '#read-parties',
    data: {
        
    },
    components: {
        'table-header': tableHeaderComponent
    }
});

