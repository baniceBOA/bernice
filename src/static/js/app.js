var toolbarOptions = [
    [{
      'header': [1, 2, 3, 4, 5, 6, false]
    }],
    ['bold', 'italic', 'underline', 'strike'], // toggled buttons
    ['blockquote', 'code-block'],

    [{
      'header': 1
    }, {
      'header': 2
    }], // custom button values
    [{
      'list': 'ordered'
    }, {
      'list': 'bullet'
    }],
    [{
      'script': 'sub'
    }, {
      'script': 'super'
    }], // superscript/subscript
    [{
      'indent': '-1'
    }, {
      'indent': '+1'
    }], // outdent/indent
    [{
      'direction': 'rtl'
    }], // text direction

    [{
      'size': ['small', false, 'large', 'huge']
    }], // custom dropdown

    [{
      'color': []
    }, {
      'background': []
    }], // dropdown with defaults from theme
    [{
      'font': []
    }],
    [{
      'align': []
    }],
    ['link', 'image'],

    ['clean'] // remove formatting button
  ];

  var quillFull = new Quill('#document-full', {
    modules: {
      toolbar: toolbarOptions,
      
    },
    theme: 'snow',
    placeholder: "Write something..."
  });

  quillFull.on('text-change', function(delta){
    var input_var = $('post_input');
    input_var.val(delta);
    
  }) 
 $("#save-btn").bind('click', function(){
  var delta = quillFull.root.innerHTML;
  var serial = delta;

    $.post('/newblog', {'post':serial}, function(data){
      if (data['post'] == 'success'){
$(".editor-full").appendTo('<div class="alert alert-success">submitted.</div>')
      }

    })
 })



 
  


 
