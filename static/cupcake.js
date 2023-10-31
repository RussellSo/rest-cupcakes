let add = document.querySelector("#add")
let formflavor = document.querySelector('#flavor')
let formrating = document.querySelector('#rating')
let formsize = document.querySelector("#size")
let cupcakeList = document.querySelector("#list")

let deleteBtn = document.querySelector("#delete")

add.addEventListener("click", async function(e) {
    e.preventDefault()
    flavor = formflavor.value
    rating = formrating.value
    size = formsize.value

    let newCupcake = await axios.post('/api/cupcakes', {flavor, rating, size})
    console.log(newCupcake)
    let cupRes = newCupcake.data.cupcake
    cupcakeList.innerHTML += `<li>Flavor: ${cupRes.flavor} <button id="delete">Delete!</button></li>`

})

deleteBtn.addEventListener("click", async function(e) {
    e.preventDefault()
    // let id = deleteBtn.parentElement.data('id')
    await axios.delete(`/api/cupcakes/${id}`)

    deleteBtn.parentElement.remove()
})


