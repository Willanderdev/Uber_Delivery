

function Mudarestado(el) {
  document.getElementById(el).classList.toggle('mostrar');
}


function atribuirvalor() {

  let coleta = document.querySelector("[name='coleta']").value;
  let entrega = document.querySelector("[name='entrega']").value;
  let veiculo = document.querySelector("[name='veículo']").value;

  document.querySelector("[name='coleta2']").value = coleta;
  document.querySelector("[name='entrega2']").value = entrega;
  document.querySelector("[name='veículo2']").value = veiculo;
}


//-----------------------------------------------------------------------------------------
function carregar() {
  let complete = document.getElementById('auto2').value;
  let input = document.querySelector("[name='nome']").value;
  let coleta = document.querySelector("[name='coleta']").value;

  if (complete.length != 0) {
    let lable = 'Endereço de ENTREGA';
    document.getElementById('lable').innerHTML = lable;
  }

  if (coleta.length != 0) {
    document.querySelector("[name='entrega']").value = input;
    document.querySelector("[name='nome']").value = '';

  }
  else {
    document.querySelector("[name='coleta']").value = input;
    document.querySelector("[name='nome']").value = '';
  }
}
//----------------------------------------------------------------------------------------------
function valor() {

  var select = document.getElementById('serv_veiculos');
  var option = select.options[select.selectedIndex];
  let distancia = document.querySelector("[name='valor_distancia']").value;
  // let valor = document.querySelector("[name='valor']").value;
  
  document.getElementById('id_veiculo2').value = option.value;
  let veiculo = document.getElementById('id_veiculo2').value;
  

  if (veiculo == '1') {
    let val_km = 8;
    let val_serv = val_km * (parseInt(distancia) / 1000)
    console.log(val_serv)
    document.querySelector("[name='valor']").value = val_serv;

  }
  else if (veiculo == '2') {
    let val_km = 15;
    let val_serv = val_km * (parseInt(distancia) / 1000);
    console.log(val_serv)
    document.querySelector("[name='valor']").value = val_serv;
  }
  else if (veiculo == '3') {
    let val_km = 30;
    let val_serv = val_km * (parseInt(distancia) / 1000);
    console.log(val_serv)
    document.querySelector("[name='valor']").value = val_serv;
  }
  else {
    let val_km = 60;
    let val_serv = val_km * (parseInt(distancia) / 1000);
    console.log(val_serv)
    document.querySelector("[name='valor']").value = val_serv;
  }
}
//--------------------------------------------------------------------------------------------------------------------------



function addressAutocomplete(containerElement, callback, options) {

  const MIN_ADDRESS_LENGTH = 3;
  const DEBOUNCE_DELAY = 300;
  var containerElement = document.getElementById('auto')
  var inputContainerElement = document.getElementById('auto1')
  var inputElement = document.getElementById('auto2')


  document.getElementById('auto2').setAttribute("placeholder", options.placeholder);


  const clearButton = document.createElement("div");
  clearButton.classList.add("clear-button");
  addIcon(clearButton);
  clearButton.addEventListener("click", (e) => {
    e.stopPropagation();
    inputElement.value = '';
    callback(null);
    clearButton.classList.remove("visible");
    closeDropDownList();
  });
  inputContainerElement.appendChild(clearButton);

  /* We will call the API with a timeout to prevent unneccessary API activity.*/
  let currentTimeout;

  /* Save the current request promise reject function. To be able to cancel the promise when a new request comes */
  let currentPromiseReject;

  /* Focused item in the autocomplete list. This variable is used to navigate with buttons */
  let focusedItemIndex;

  /* Process a user input: */
  inputElement.addEventListener("input", function (e) {
    const currentValue = this.value;

    /* Close any already open dropdown list */
    closeDropDownList();


    // Cancel previous timeout
    if (currentTimeout) {
      clearTimeout(currentTimeout);
    }

    // Cancel previous request promise
    if (currentPromiseReject) {
      currentPromiseReject({
        canceled: true
      });
    }

    if (!currentValue) {
      clearButton.classList.remove("visible");
    }

    // Show clearButton when there is a text
    clearButton.classList.add("visible");

    // Skip empty or short address strings
    if (!currentValue || currentValue.length < MIN_ADDRESS_LENGTH) {
      return false;
    }

    /* Call the Address Autocomplete API with a delay */
    currentTimeout = setTimeout(() => {
      currentTimeout = null;

      /* Create a new promise and send geocoding request */
      const promise = new Promise((resolve, reject) => {
        currentPromiseReject = reject;

        // The API Key provided is restricted to JSFiddle website
        // Get your own API Key on https://myprojects.geoapify.com
        const apiKey = "6dc7fb95a3b246cfa0f3bcef5ce9ed9a";

        var url = `https://api.geoapify.com/v1/geocode/autocomplete?text=${encodeURIComponent(currentValue)}&format=json&limit=5&apiKey=${apiKey}`;

        fetch(url)
          .then(response => {
            currentPromiseReject = null;

            // check if the call was successful
            if (response.ok) {
              response.json().then(data => resolve(data));
            } else {
              response.json().then(data => reject(data));
            }
          });
      });

      promise.then((data) => {
        // here we get address suggestions
        currentItems = data.results;

        /*create a DIV element that will contain the items (values):*/
        const autocompleteItemsElement = document.createElement("div");
        autocompleteItemsElement.setAttribute("class", "autocomplete-items");
        inputContainerElement.appendChild(autocompleteItemsElement);

        /* For each item in the results */
        data.results.forEach((result, index) => {
          /* Create a DIV element for each element: */
          const itemElement = document.createElement("div");
          /* Set formatted address as item value */
          itemElement.innerHTML = result.formatted;
          autocompleteItemsElement.appendChild(itemElement);

          /* Set the value for the autocomplete text field and notify: */
          itemElement.addEventListener("click", function (e) {
            inputElement.value = currentItems[index].formatted;
            callback(currentItems[index]);
            /* Close the list of autocompleted values: */
            closeDropDownList();
          });
        });

      }, (err) => {
        if (!err.canceled) {
          console.log(err);
        }
      });
    }, DEBOUNCE_DELAY);
  });

  /* Add support for keyboard navigation */
  inputElement.addEventListener("keydown", function (e) {
    var autocompleteItemsElement = containerElement.querySelector(".autocomplete-items");
    if (autocompleteItemsElement) {
      var itemElements = autocompleteItemsElement.getElementsByTagName("div");
      if (e.keyCode == 40) {
        e.preventDefault();
        /*If the arrow DOWN key is pressed, increase the focusedItemIndex variable:*/
        focusedItemIndex = focusedItemIndex !== itemElements.length - 1 ? focusedItemIndex + 1 : 0;
        /*and and make the current item more visible:*/
        setActive(itemElements, focusedItemIndex);
      } else if (e.keyCode == 38) {
        e.preventDefault();

        /*If the arrow UP key is pressed, decrease the focusedItemIndex variable:*/
        focusedItemIndex = focusedItemIndex !== 0 ? focusedItemIndex - 1 : focusedItemIndex = (itemElements.length - 1);
        /*and and make the current item more visible:*/
        setActive(itemElements, focusedItemIndex);
      } else if (e.keyCode == 13) {
        /* If the ENTER key is pressed and value as selected, close the list*/
        e.preventDefault();
        if (focusedItemIndex > -1) {
          closeDropDownList();
        }
      }
    } else {
      if (e.keyCode == 40) {
        /* Open dropdown list again */
        var event = document.createEvent('Event');
        event.initEvent('input', true, true);
        inputElement.dispatchEvent(event);
      }
    }
  });

  function setActive(items, index) {
    if (!items || !items.length) return false;

    for (var i = 0; i < items.length; i++) {
      items[i].classList.remove("autocomplete-active");
    }

    /* Add class "autocomplete-active" to the active element*/
    items[index].classList.add("autocomplete-active");

    // Change input value and notify
    inputElement.value = currentItems[index].formatted;
    callback(currentItems[index]);
  }

  function closeDropDownList() {
    const autocompleteItemsElement = inputContainerElement.querySelector(".autocomplete-items");
    if (autocompleteItemsElement) {
      inputContainerElement.removeChild(autocompleteItemsElement);
    }

    focusedItemIndex = -1;
  }

  function addIcon(buttonElement) {
    const svgElement = document.createElementNS("http://www.w3.org/2000/svg", 'svg');
    svgElement.setAttribute('viewBox', "0 0 24 24");
    svgElement.setAttribute('height', "24");

    const iconElement = document.createElementNS("http://www.w3.org/2000/svg", 'path');
    iconElement.setAttribute("d", "M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z");
    iconElement.setAttribute('fill', 'currentColor');
    svgElement.appendChild(iconElement);
    buttonElement.appendChild(svgElement);
  }

  /* Close the autocomplete dropdown when the document is clicked. 
    Skip, when a user clicks on the input field */
  document.addEventListener("click", function (e) {
    if (e.target !== inputElement) {
      closeDropDownList();
    } else if (!containerElement.querySelector(".autocomplete-items")) {
      // open dropdown list again
      var event = document.createEvent('Event');
      event.initEvent('input', true, true);
      inputElement.dispatchEvent(event);
    }
  });
}

addressAutocomplete(document.getElementById("autocomplete-container"), (data) => {
  console.log("Selected option: ");
  console.log(data);
}, {
  placeholder: "digite o endereço aqui"
});


// -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// set up jQuery ajax object to always send CSRF token in headers
// https://docs.djangoproject.com/en/2.2/ref/csrf/#ajax
var getCookie = function (name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var csrfSafeMethod = function (method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
  }
});

//chamando Ajax com jquery
$(document).ready(function () {

  $('.carrega_conteudo').click(function () {

    // var carrega_url = this.id;
    // carrega_url = carrega_url;


    let requisition = $.ajax({
      url: 'solicite.html',
      type: 'POST',
      dataType: 'html'
    });

    requisition.done(function (data) {
      $('#solicite').html(data);
    });

  });

});



//desabilita funçao de autorefresh do botão submiy
function debug(e) {
  e.preventDefault();
};



//---------------------------------------------------------------------------------------------------------------------------------------------------------------------
// chamando ajax com javascript


// var httpRequest;

// function fazerRequisicao(url, destino) {

//   // document.getElementById(destino).innerHTML = "<center><img src='loader.gif'></center>";

//   if (window.XMLHttpRequest) {
//     httpRequest = new XMLHttpRequest();
//   } else if (window.ActiveXObject) {
//     try {

//       httpRequest = new ActiveXObject("Msxml2.XMLHTTP");

//     } catch (e) {

//       try {

//         httpRequest = new ActiveXObject("Microsoft.XMLHTTP");

//       } catch (e) {

//         alert("Impossível instanciar o objeto XMLHttpRequest para esse navegador/versão");

//       }

//     }
//   }

//   if (!httpRequest) {
//     alert("Erro ao tentar criar uma instância do objeto XMLHttpRequest");
//     return false;
//   }

//   httpRequest.onreadystatechange = situacaoRequisicao;

//   httpRequest.open("GET", url);
//   httpRequest.send();

// }

// function situacaoRequisicao() {

//   if (httpRequest.readyState == 4) {

//     if (httpRequest.status == 200) {

//       document.getElementById('div_conteudo').innerHTML = httpRequest.responseText;

//     }

//   }

// }

//------------------------------------------------------------------------------------------------------------------------------------




    // success: function (data) {
    //   alert(url);
    //   $('#div_conteudo').html(data);
    // },

    // beforeSend: function () {
    //   $('#loader').css({ display: "block" });
    // },

    // complete: function () {
    //   $('#loader').css({ display: "none" });
    // }

