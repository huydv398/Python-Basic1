{% extends 'index.html' %}
{% block body %}
<h2 class="text-danger container">Danh sách sinh viên</h2>

<table class="table container">
<thead>
    <tr>
    <th>MSV</th>
    <th>Họ và Tên</th>
    <th>Ngày sinh</th>
    <th>Quê quán</th>
    <th>Địa chỉ hiện tại</th>
    <th>Số điện thoại</th>
    <th>CCCD</th>
    <th>Giới tính</th>
    <th>Time update</th>
    <th>Email</th>
    <th>Chức năng</th>
    </tr>
</thead>
<tbody>

    {% for id in result %}
    <tr>
    <td>{{id[0]}}</td>
    <td>{{id[1]}}</td>
    <td>{{id[2]}}</td>
    <td>{{id[3]}}</td>
    <td>{{id[4]}}</td>
    <td>{{id[5]}}</td>
    <td>{{id[6]}}</td>
    <td>{{id[7]}}</td>
    <td>{{id[8]}}</td>
    <td>{{id[9]}}</td>
    <td>
        <div class="dropdown">
            <button class="btn btn-success dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                <i class="icofont-pencil"></i>
            </button>
            <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Delete VM</a></li>
            
            <li><button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#myModal">
                VM del
            </button></li>
            <form method="POST" action="/delvm"> 
                <!-- The Modal -->
                <div class="modal" id="myModal">
                <div class="modal-dialog">
                    <div class="modal-content">

                    <!-- Modal Header -->
                    <div class="modal-header">
                        <h4 class="modal-title">Modal Heading</h4>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>

                    <!-- Modal body -->
                    <div class="modal-body">
                        Xac nhan xoa VM: {{id[1]}}, is_ins: {{id[0]}}

                    </div>
                    <input type="hidden" name="MSV" value="{{id[0]}}">
                    <!-- Modal footer -->
                    <div class="modal-footer">
                        <button type="button" class="btn btn-success" data-bs-dismiss="modal">Cancle</button>
                        <button type="submit" class="btn btn-danger" data-bs-dismiss="modal">Delete</button>
                    </div>
                </div>
                </form>
            </ul>
            
            </div>
            </div>
        </div>
    </td>
    </tr>
    {% endfor %}
</tbody>
</table>

{% endblock %}

<form method="POST" action="/deluser"> 
    <!-- The Modal -->
    <div class="modal" id="myModal">
      <div class="modal-dialog">
        <div class="modal-content">

          <!-- Modal Header -->
          <div class="modal-header">
            <h4 class="modal-title">Modal Heading</h4>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>

          <!-- Modal body -->
          <div class="modal-body">
            Xac nhan xoa Sinh vien: {{id[1]}}, MSV: {{id[0]}}

          </div>
          <input type="hidden" name="MSV" value="{{id[0]}}">
          <!-- Modal footer -->
          <div class="modal-footer">
            <button type="button" class="btn btn-success" data-bs-dismiss="modal">Cancle</button>
            <button type="submit" class="btn btn-danger" data-bs-dismiss="modal">Delete</button>
          </div>
      </div>
    </form>
</ul>
<!-- Button to Open the Modal 
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
  Xóa Sinh viên
</button>-->
