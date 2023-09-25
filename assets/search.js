import pokemon from 'pokemontcgsdk'
pokemon.configure({ 'api.Key': '' })

const initApp = () => {
	const searchBtn = document.getElementById('search-btn')
	const showResultsTable = document.getElementById('search-results-table')
	const showResultsImage = document.getElementById('search-results-image')
	const searchTable = document.getElementById('search-table')
	const searchForm = document.getElementById('search-form')
	const searchLoading = document.getElementById('search-loading')
	const searchHeader = document.getElementById('search-header')
	const tableBtn = document.getElementById('table-button')
	const viewBtn = document.getElementById('dropdownViewButton')
	const sortBtn = document.getElementById('dropdownSortButton')
	const sortDiv = document.getElementById('sort-div')
	const orderBtn = document.getElementById('dropdownOrderButton')
	const orderDiv = document.getElementById('order-div')
	const searchTitle = document.getElementById('search')
	const submitBtn = document.getElementById('submit-button')
	const submitForm = document.getElementById('submit-form')

	const addToCollection = (e) => {
		e.preventDefault()
		const value = e.target.value
		const button = document.getElementById(value)
		button.innerText = 'Remove'
		button.style.cssText += 'color:red'
		button.onclick = removeFromCollection

		const input = document.createElement('input')
		input.classList.add('hidden')
		input.value = value
		input.name = 'card_id'
		input.id = `card_${value}`
		input.type = 'text'
		submitForm.insertBefore(input, submitBtn)
	}

	const removeFromCollection = (e) => {
		e.preventDefault()
		const value = e.target.value
		const button = document.getElementById(value)
		button.innerText = 'Add'
		button.style.cssText += 'color:blue'
		button.onclick = addToCollection

		const input = document.getElementById(`card_${value}`)
		input.remove()
	}

	const search = (e) => {
		e.preventDefault()
		const input = document.getElementById('search-bar').value.toLowerCase()
		if (input.length < 3) {
			searchTitle.innerText =
				'Please enter a valid pokemon name, 3 characters minimum!'
			searchTitle.style.cssText += 'color:red'
			return
		} else {
			searchTitle.innerText = 'Search'
			searchTitle.style.cssText += 'color:black'
		}

		const classArray = ['p-3']
		searchForm.classList.toggle('flex')
		searchForm.classList.toggle('hidden')
		searchLoading.classList.toggle('hidden')
		pokemon.card.where({ q: `name:${input}` }).then((result) => {
			for (let i = 0; i < result.data.length; i++) {
				// image results
				const img = document.createElement('img')
				showResultsImage.appendChild(img)
				img.src = result.data[i].images.small
				img.alt = result.data[i].name
				img.classList.add('mb-6', 'w-full', 'cursor-pointer')
				img.width = 'auto'
				img.height = 'auto'

				// table results
				const tr = document.createElement('tr')
				showResultsTable.appendChild(tr)

				const tdSet = document.createElement('td')
				tr.appendChild(tdSet)
				tdSet.innerHTML = result.data[i].set.name
				tdSet.classList.add(...classArray)

				const tdNum = document.createElement('td')
				tr.appendChild(tdNum)
				tdNum.innerHTML = result.data[i].number
				tdNum.classList.add(...classArray)

				const tdName = document.createElement('td')
				tr.appendChild(tdName)
				tdName.innerHTML = result.data[i].name
				tdName.classList.add(...classArray)

				const tdRarity = document.createElement('td')
				tr.appendChild(tdRarity)
				tdRarity.innerHTML = result.data[i].rarity
				tdRarity.classList.add(...classArray)

				const tdTypes = document.createElement('td')
				tr.appendChild(tdTypes)
				tdTypes.innerHTML = result.data[i].types
				tdTypes.classList.add(...classArray)

				const tdSupertype = document.createElement('td')
				tr.appendChild(tdSupertype)
				tdSupertype.innerHTML = result.data[i].supertype
				tdSupertype.classList.add(...classArray)

				const tdSubtypes = document.createElement('td')
				tr.appendChild(tdSubtypes)
				tdSubtypes.innerHTML = result.data[i].subtypes
				tdSubtypes.classList.add(...classArray)

				const tdPrice = document.createElement('td')
				tr.appendChild(tdPrice)
				if (result.data[i].tcgplayer.prices === undefined) {
					tdPrice.innerHTML = 'NA'
				} else if (result.data[i].tcgplayer.prices.normal) {
					tdPrice.innerHTML = `$${result.data[
						i
					].tcgplayer.prices.normal.market.toFixed(2)}`
				} else if (result.data[i].tcgplayer.prices.holofoil) {
					tdPrice.innerHTML = `$${result.data[
						i
					].tcgplayer.prices.holofoil.market.toFixed(2)}`
				} else if (result.data[i].tcgplayer.prices.reverseHolofoil) {
					tdPrice.innerHTML = `$${result.data[
						i
					].tcgplayer.prices.reverseHolofoil.market.toFixed(2)}`
				} else if (result.data[i].tcgplayer.prices.unlimited) {
					tdPrice.innerHTML = `$${result.data[
						i
					].tcgplayer.prices.unlimited.market.toFixed(2)}`
				} else if (result.data[i].tcgplayer.prices.unlimitedHolofoil) {
					tdPrice.innerHTML = `$${result.data[
						i
					].tcgplayer.prices.unlimitedHolofoil.market.toFixed(2)}`
				} else {
					tdPrice.innerHTML = '$0.00'
				}
				tdPrice.classList.add(...classArray)

				const tdCollection = document.createElement('td')
				tr.appendChild(tdCollection)
				tdCollection.classList.add(...classArray)

				const addCollection = document.createElement('button')
				addCollection.type = 'submit'
				addCollection.id = result.data[i].id
				addCollection.value = result.data[i].id
				addCollection.innerText = 'Add'
				addCollection.style.cssText += 'color:blue'
				addCollection.classList.add(
					'hover:text-blue-700',
					'active:text-blue-300'
				)
				addCollection.onclick = addToCollection
				tdCollection.appendChild(addCollection)
			}
			searchLoading.classList.toggle('hidden')
			searchHeader.classList.toggle('hidden')
			searchForm.classList.toggle('hidden')
			searchForm.classList.toggle('flex')
			tableBtn.classList.toggle('sm:hidden')
			tableBtn.classList.toggle('sm:flex')
			submitBtn.classList.toggle('hidden')
		})
	}
	if (searchBtn) {
		searchBtn.addEventListener('click', search)
	}

	const toggleSortBtn = () => {
		sortDiv.classList.toggle('hidden')
	}

	const toggleOrderBtn = () => {
		orderDiv.classList.toggle('hidden')
	}

	if (sortBtn) {
		sortBtn.addEventListener('click', toggleSortBtn)
	}

	if (orderBtn) {
		orderBtn.addEventListener('click', toggleOrderBtn)
	}

	// view button functionality
	const toggleView = () => {
		searchTable.classList.toggle('sm:flex')
		searchTable.classList.toggle('sm:hidden')
		showResultsImage.classList.toggle('sm:hidden')
		showResultsImage.classList.toggle('sm:grid')
		if (viewBtn.innerText == 'Table') {
			viewBtn.innerText = 'Image'
		} else if (viewBtn.innerText == 'Image') {
			viewBtn.innerText = 'Table'
		}
	}

	if (viewBtn) {
		viewBtn.addEventListener('click', toggleView)
	}
}

document.addEventListener('DOMContentLoaded', initApp)
