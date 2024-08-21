let pet=[
  {"type":"dog","breed":"Dachshund","age":"2 years","gender":"Male","weight":"15.7 kg","title":"Bunzo","src":"assets/bunzo.jpg"},
  {"type":"cat","breed":"American Curl","age":"1 year","gender":"Female","weight":"12 Kg","title":"Kate","src":"assets/kate.jpg"},
  {"type":"cat","breed":"Maine Coon","age":"10 months","gender":"Female","weight":"10Kg","title":"Sadie","src":"https://wallpapers.com/images/hd/crazy-cat-pictures-700-x-933-xhotsmvv6906rl9h.jpg"},
  {"type":"cat","breed":"Bombay Cat","age":"1.5 years","gender":"Male","weight":"15 Kg","title":"Ray","src":"https://wallpapers.com/images/hd/crazy-cat-pictures-700-x-933-tk3s09u6cqnskxpn.jpg"},
  {"type":"cat","breed":"American Bobtail","age":"2 years","gender":"Male","weight":"13.6 Kg","title":"Lulu","src":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtrTL-M1bZv6vzelXpyZg0h5VNjCUZcByggg&s"},
  {"type":"dog","breed":"Rottweiler","age":"4 years","gender":"Male","weight":"50 kg","title":"Bruno","src":"https://www.eastmidlandsdogrescue.org/wp-content/uploads/2024/05/bonnie-700x933.jpg"},
  {"type":"dog","breed":"Pitbull","age":"6 months","gender":"Female","weight":"2.4 kg","title":"Loui","src":"https://novasroyal.pet/wp-content/uploads/2024/06/img_3951-700x933.jpeg"},
  {"type":"dog","breed":"Pug","age":"1 years","gender":"Male","weight":"10 kg","title":"John","src":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTi4qWkCIcUSy8If5vXIJWOIjSczAVyuO70sw&s"},
  {"type":"dog","breed":"Poodle","age":"2 years","gender":"Female","weight":"20 kg","title":"Dex","src":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2QDJ-R4MG1VNO56smdMqYAL-qX0Y-uW0_9g&s"},];
  const container = document.getElementById('accordion');
  const inputBtn = document.getElementById("input-btn");
  const inputEl = document.getElementById("name");
  const heading=document.getElementById("title");
  
  function getInputVal() {
    display(inputEl.value.trim());
  }
  
  inputBtn.addEventListener("click", getInputVal);
  
  function display(val){
      container.innerHTML="";
      heading.innerHTML="Showing results of: "+val.charAt(0).toUpperCase() + val.slice(1);
  
      var search=val.includes("dog")?"dog":"cat";
  
      pet.forEach((result, idx) => {
    // Create card element
    const card = document.createElement('div');
    card.classList = 'card-body';
    
    // Construct card content
    //added sorting as well
    const content = (result.type==val)||val.toLowerCase().includes(result.breed.toLowerCase())? `
      <div class="col-lg-4 col-md-6 mb-4">
                    <div class="card d-flex" style="background-color: rgb(206, 249, 255); border-color: rgb(49, 173, 255); border-radius: 2vw; height: 100%;">
                        <img class="card-img-top p-3" src=${result.src} style="border-radius: 2vw; height: 100%;">
                        <div class="card-body text-center">
                            <h3 class="card-text fs-2 text-body-emphasis">${result.title}</h3>
                        </div>
                        <div class="text-center">
                        <h4>Breed: ${result.breed}</h4>
                        <h4>Age: ${result.age}</h4>
                        <h4>Gender: ${result.gender}</h4>
                        <h5>Weight: ${result.weight}</h5>
                          <div>
                    </div>
                </div>
    `:"";
  
    // Append newyly created card element to the container
    container.innerHTML += content;
  })
  
  }