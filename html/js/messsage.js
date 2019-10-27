var APP_ID = 'E2TMVL0rL8I8ypUTIr2z80Wu-gzGzoHsz';
var APP_KEY = 'ibpkh3Ppxezxc1JMt74L2XNG';

AV.init({
  appId: APP_ID,
  appKey: APP_KEY
});

var query = new AV.Query('Message');
query.find()
    .then(function (messages) {
        let array=messages.map((item)=>item.attributes)
        array.forEach((item)=>{
            let li=document.createElement('li')
            li.innerText=`${item.name}:${item.content}`
            let messageList=document.querySelector('#messageList')
            messageList.appendChild(li)
        })
    })

let myForm=document.querySelector('#postMessageForm')

myForm.addEventListener('submit',function(e){
    e.preventDefault()
    let content=myForm.querySelector('input[name=content]').value
    let name=myForm.querySelector('input[name=name]').value
    var Message = AV.Object.extend('Message');
    var message=new Message();
    message.save({
        'name':name,
        'content':content
    }).then(function (object) {
        let li = document.createElement('li')
        li.innerText = `${object.attributes.name}:${object.attributes.content}`
        let messageList = document.querySelector('#messageList')
        messageList.appendChild(li)
        myForm.querySelector('input[name=content]').value=''
        name=myForm.querySelector('input[name=name]').value=''
      })
})