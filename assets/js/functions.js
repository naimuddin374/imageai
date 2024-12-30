let name="";
let bg="";
let filter_name="";
let base64String = "";
let base64_image="";
let base64String_bg = "";
let base64String_filter ="";
let base64_bg="";
let base64_filter="";
let filename="";
let image_path="";
let base64_gif="";
let gif_name="";
let base64String_gif="";
let current_state="";

        function change_image()
        {
          input.click();
        }
        
        // function imageUploaded() {
        //   var file = document.getElementById('fileId').files[0];

        //     console.log(file)
        //     name=file["name"]
        //     console.log(name)
        
        //     var reader = new FileReader();
        //     console.log("next");
            
        //     reader.onload = function () {
        //         base64String = reader.result.replace("data:", "")
        //             .replace(/^.+,/, "");
        
        //         imageBase64Stringsep = base64String;
        
        //         // alert(imageBase64Stringsep);
        //         //console.log(base64String);
        //         base64_image=base64String
        //     }
        //     reader.readAsDataURL(file);
        // }
        
        function uploadApi()
        {
            random=Date.now()
            var namefile =  random + name;
            console.log(namefile)
            filename=namefile
            image_path="http://127.0.0.1:8000/media/uploaded/"+filename;
            console.log(image_path)

            //state setup
            current_state=filename

            //var formData = new FormData();
            //formData.append('image', base64_image);
            var formData={"name":filename, "image":base64_image}
            var output=JSON.stringify(formData);
            
            console.log(output);

            fetch('http://127.0.0.1:8000/upload/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  // document.getElementById("image").src = image_path;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }

        function bgRemove()
        {

            //var formData = new FormData();
            //formData.append('image', base64_image);
            let filename_bg="bg"+filename
            image_path="http://127.0.0.1:8000/media/background_remove/"+filename_bg;
            var formData={"name":filename_bg, "image":base64_image}
            var output=JSON.stringify(formData); 
            console.log(output);

            //state setup
            current_state=filename_bg
            document.getElementById('loadId').style.display = "block";
            fetch('http://127.0.0.1:8000/background-remove/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  //console.log("image-path = "+image_path);
                  // document.getElementById("image").src = image_path;
                  document.getElementById('loadId').style.display = "none";
                  let imgTag = `<img src="${image_path}" alt="image">`;
                  dropArea.innerHTML = imgTag;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }
        function bgBlur()
        {

            //var formData = new FormData();
            //formData.append('image', base64_image);
            let filename_bg="bgblur"+filename
            image_path="http://127.0.0.1:8000/media/background_blur/"+filename_bg;
            var formData={"name":filename_bg, "image":base64_image}
            var output=JSON.stringify(formData);
            console.log(output);

            //state setup
            current_state=filename_bg

            document.getElementById('loadId').style.display = "block";
            fetch('http://127.0.0.1:8000/background-blur/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  //console.log("image-path = "+image_path);
                  // document.getElementById("image").src = image_path;
                  document.getElementById('loadId').style.display = "none";
                  let imgTag = `<img src="${image_path}" alt="image">`;
                  dropArea.innerHTML = imgTag;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }

        function bgchange(value)
        {

            //var formData = new FormData();
            //formData.append('image', base64_image);
            let filename_bg="bgchange"+value+filename
            image_path="http://127.0.0.1:8000/media/background_change/"+filename_bg;
            var formData={"name":filename_bg,"name1":value, "image":base64_image}
            var output=JSON.stringify(formData);
            console.log(output);

            //state setup
            current_state=filename_bg

            document.getElementById('loadId').style.display = "block";
            fetch('http://127.0.0.1:8000/background-change/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  //console.log("image-path = "+image_path);
                  // document.getElementById("image").src = image_path;
                  document.getElementById('loadId').style.display = "none";
                  let imgTag = `<img src="${image_path}" alt="image">`;
                  dropArea.innerHTML = imgTag;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }

        function filter(value)
        {

            //var formData = new FormData();
            //formData.append('image', base64_image);
            let filename_bg="filter"+value+filename
            image_path="http://127.0.0.1:8000/media/after_filtering/"+filename_bg;
            var formData={"name":filename_bg,"name1":value, "image":base64_image}
            var output=JSON.stringify(formData);
            console.log(output);

            //state setup
            current_state=filename_bg

            document.getElementById('loadId').style.display = "block";

            fetch('http://127.0.0.1:8000/style/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  //console.log("image-path = "+image_path);
                  // document.getElementById("image").src = image_path;
                  document.getElementById('loadId').style.display = "none";
                  let imgTag = `<img src="${image_path}" alt="image">`;
                  dropArea.innerHTML = imgTag;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }


        function facefocused()
        {

            //var formData = new FormData();
            //formData.append('image', base64_image);
            let filename_bg="ff"+filename
            image_path="http://127.0.0.1:8000/media/face_focused/"+filename_bg;
            var formData={"name":filename_bg, "image":base64_image}
            var output=JSON.stringify(formData);
            console.log(output);

            //state setup
            current_state=filename_bg

            document.getElementById('loadId').style.display = "block";

            fetch('http://127.0.0.1:8000/face_focused/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  //console.log("image-path = "+image_path);
                  // document.getElementById("image").src = image_path;
                  document.getElementById('loadId').style.display = "none";
                  let imgTag = `<img src="${image_path}" alt="image">`;
                  dropArea.innerHTML = imgTag;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }

        function beautification()
        {
          
            //Hello
            //var formData = new FormData();
            //formData.append('image', base64_image);
            let filename_bg="beauty"+filename
            image_path="http://127.0.0.1:8000/media/beautification/"+filename_bg;
            var formData={"name":filename_bg,"w":0.3,"s":0.3,"image":base64_image}
            var output=JSON.stringify(formData); 
            console.log(output);

            //state setup
            current_state=filename_bg

            document.getElementById('loadId').style.display = "block";

            fetch('http://127.0.0.1:8000/beauty/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  //console.log("image-path = "+image_path);
                  // document.getElementById("image").src = image_path;
                  document.getElementById('loadId').style.display = "none";
                  let imgTag = `<img src="${image_path}" alt="image">`;
                  dropArea.innerHTML = imgTag;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }

        function bgUploaded() {
          var file = document.getElementById('bgId').files[0];
          console.log(file)
          bg=file["name"]
          console.log(bg)
      
          var reader = new FileReader();
          console.log("bg_next")
          
          reader.onload = function () {
             base64String_bg = reader.result.replace("data:", "")
                  .replace(/^.+,/, "");
      
              imageBase64Stringsep_bg = base64String_bg;
      
              // alert(imageBase64Stringsep);
              //console.log(base64String);
              base64_bg=base64String_bg
          }
          reader.readAsDataURL(file);
      }
        
        function custombg()
        {

            random=Date.now()
            var bgfile =  random + bg;
            console.log(bgfile)
            bgname=bgfile

            let filename_bg="bgchange"+bgname+filename
            image_path="http://127.0.0.1:8000/media/background_change/"+filename_bg;

            var formData={"name1":filename_bg,"name2":bgname, "image1":base64_image, "image2":base64_bg}
            var output=JSON.stringify(formData);
            console.log(output);

            //state setup
            current_state=filename_bg

            document.getElementById('loadId').style.display = "block";

            fetch('http://127.0.0.1:8000/custom-background/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  //console.log("image-path = "+image_path);
                  // document.getElementById("image").src = image_path;
                  document.getElementById('loadId').style.display = "none";
                  let imgTag = `<img src="${image_path}" alt="image">`;
                  dropArea.innerHTML = imgTag;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }



        function filterUploaded() {
          var file = document.getElementById('filterId').files[0];
          console.log(file)
          filter_name=file["name"]
          console.log(filter_name)
      
          var reader = new FileReader();
          console.log("filter_next")
          
          reader.onload = function () {
             base64String_filter = reader.result.replace("data:", "")
                  .replace(/^.+,/, "");
      
              imageBase64Stringsep_filter = base64String_filter;
      
              // alert(imageBase64Stringsep);
              //console.log(base64String);
              base64_filter=base64String_filter
          }
          reader.readAsDataURL(file);
      }
        
        function customfilter()
        {

            random=Date.now()
            var filterfile =  random + filter_name;
            console.log(filterfile)
            filtername=filterfile

            let filename_filter="bgchange"+filtername+filename
            image_path="http://127.0.0.1:8000/media/after_filtering/"+filename_filter;

            var formData={"name1":filename_filter,"name2":filtername, "image1":base64_image, "image2":base64_filter}
            var output=JSON.stringify(formData);
            console.log(output);

            //state setup
            current_state=filename_filter

            document.getElementById('loadId').style.display = "block";

            fetch('http://127.0.0.1:8000/custom-filter/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  //console.log("image-path = "+image_path);
                  // document.getElementById("image").src = image_path;
                  document.getElementById('loadId').style.display = "none";
                  let imgTag = `<img src="${image_path}" alt="image">`;
                  dropArea.innerHTML = imgTag;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }

        function overlappedfilter()
        {

            //var formData = new FormData();
            //formData.append('image', base64_image);
            let filename_bg="overlappedfilter"+filename
            image_path="http://127.0.0.1:8000/media/after_filtering/"+filename_bg;
            var formData={"name1":filename_bg,"name2":name, "image1":base64_image,"image2":base64_image}
            var output=JSON.stringify(formData);
            console.log(output);

            //state setup
            current_state=filename_bg

            document.getElementById('loadId').style.display = "block";

            fetch('http://127.0.0.1:8000/custom-filter/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  //console.log("image-path = "+image_path);
                 // document.getElementById("image").src = image_path;
                 document.getElementById('loadId').style.display = "none";
                 let imgTag = `<img src="${image_path}" alt="image">`;
                 dropArea.innerHTML = imgTag;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }

        function variant()
        {

            console.log("Success")
            //var formData = new FormData();
            //formData.append('image', base64_image);
            let filename_v="variant_"+filename
            image_path="http://127.0.0.1:8000/media/variant_images/"+filename_v;
            var formData={"name":filename_v, "image":base64_image}
            var output=JSON.stringify(formData);
            console.log(output);

            //state setup
            current_state=filename_v

            document.getElementById('loadId').style.display = "block";

            fetch('http://127.0.0.1:8000/variant/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  //console.log("image-path = "+image_path);
                  // document.getElementById("image").src = image_path;
                  document.getElementById('loadId').style.display = "none";
                  let imgTag = `<img src="${image_path}" alt="image">`;
                  dropArea.innerHTML = imgTag;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }

        function make_gif(value)
        {
            let filename_bg="bg"+filename+"___.png"
            let output_gif=value+filename+"____.gif"
            image_path="http://127.0.0.1:8000/media/after_gif/"+output_gif;
            var formData={"input_name":filename,"bg_remove":filename_bg,"gif":value,"output":output_gif}
            var output=JSON.stringify(formData);
            console.log(output);

            //state setup
            current_state=output_gif

            document.getElementById('loadId').style.display = "block";

            fetch('http://127.0.0.1:8000/gif/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                },
                body: output,
              })
                .then((response) => response.json())
                .then((data) => {
                  console.log('Success:', data);
                  //console.log("image-path = "+image_path);
                  // document.getElementById("image").src = image_path;
                  document.getElementById('loadId').style.display = "none";
                  let imgTag = `<img src="${image_path}" alt="image">`;
                  dropArea.innerHTML = imgTag;
                })
                .catch((error) => {
                  console.error('Error:', error);
                })

        }

        // async function download(image_path) {
        //   // const image = await fetch(image_path)
        //   // const imageBlog = await image.blob()
        //   const imageURL = image_path
        
        //   const link = document.createElement('a')
        //   link.href = imageURL
        //   link.download = current_state
        //   document.body.appendChild(link)
        //   link.click()
        //   document.body.removeChild(link)
        // }

        function downloadImage(url, name){
          fetch(url)
            .then(resp => resp.blob())
            .then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                // the filename you want
                a.download = name;
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
            })
            .catch(() => alert('An error sorry'));

    }


          function download(){
            url=image_path;
            dname=current_state;
            downloadImage(url,dname);
          }
        
        























        // function gifUploaded() {
        //   var file = document.getElementById('gifId').files[0];
        //   console.log(file)
        //   gif_name=file["name"]
        //   console.log(gif_name)
      
        //   var reader = new FileReader();
        //   console.log("gif_next")
          
        //   reader.onload = function () {
        //      base64String_gif = reader.result.replace("data:", "")
        //           .replace(/^.+,/, "");
      
        //       imageBase64Stringsep_gif = base64String_gif;
      
        //       // alert(imageBase64Stringsep);
        //       //console.log(base64String);
        //       base64_gif=base64String_gif
        //       console.log("hello")
        //       console.log(base64_gif)


        //   }

        //   console.log("Hellooojkasdhgsahkjsdahkjas")
          
        //   reader.readAsDataURL(file);
        
        // }

        


        // function custom_gif()
        // {
        //     let filename_bg="bg"+filename+"___.png"
        //     let output_gif=gif_name+filename+"____.gif"
        //     image_path="http://127.0.0.1:8000/media/after_gif/"+output_gif;
        //     var formData={"input_name":filename,"bg_remove":filename_bg,"gif":gif_name,"output":output_gif,"gif_image":base64_gif}
        //     var output=JSON.stringify(formData);

            
        //     console.log(output);

        //     fetch('http://127.0.0.1:8000/custom-gif/', {
        //         method: 'POST', // or 'PUT'
        //         headers: {
        //           'Content-Type': 'application/json',
        //         },
        //         body: output,
        //       })
        //         .then((response) => response.json())
        //         .then((data) => {
        //           console.log('Success:', data);
        //           //console.log("image-path = "+image_path);
        //           document.getElementById("image").src = image_path;
        //         })
        //         .catch((error) => {
        //           console.error('Error:', error);
        //         })

        // }


    
        function show() {

            console.log(image_path)
            image.src =image_path
            console.log(image_path)
            console.log(image.src)
 
            //document.getElementById("btnID")
              //     .style.display = "none";
        }



        
