import pokemon from 'pokemontcgsdk';
pokemon.configure({ 'api.Key': 'bd895527-41d0-417e-a109-3667e7b8dddb' })

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
	const searchTitle = document.getElementById('search')
	const submitBtn = document.getElementById('submit-button')
	const submitForm = document.getElementById('submit-form')
	const images = document.querySelectorAll('.images')

	const imageSelect = (e) => {
		e.preventDefault()
		const card_id = e.target.id
		const image = document.getElementById(card_id)
		image.style.cssText += 'border: 2px solid blue'
		image.onclick = imageDeselect

		const input = document.createElement('input')
		input.classList.add('hidden')
		input.value = card_id.replace('image_', '')
		input.name = 'card_id'
		input.id = `card_${card_id}`
		input.type = 'text'
		submitForm.insertBefore(input, submitBtn)
	}

	const imageDeselect = (e) => {
		e.preventDefault()
		const card_id = e.target.id
		const image = document.getElementById(card_id)
		image.style.cssText += 'border: none'
		image.onclick = imageSelect

		const input = document.getElementById(`card_${value}`)
		input.remove()
	}

	if (images) {
		images.forEach((item) => {
			item.onclick = imageSelect
		})
	}

	const sortTable = (sortBy) => {
		const table = document.getElementById('card-table')
		let switching = true
		let rows,
			i,
			x,
			y,
			shouldSwitch,
			dir = 'asc',
			switchCount = 0
		while (switching) {
			switching = false
			rows = table.rows
			for (i = 1; i < rows.length - 1; i++) {
				shouldSwitch = false
				x = rows[i].getElementsByTagName('TD')[sortBy]
				y = rows[i + 1].getElementsByTagName('TD')[sortBy]
				if (sortBy == 7) {
					if (dir == 'asc') {
						if (
							parseFloat(x.innerHTML.replace('$', '').replace('NA', '0.00')) >
							parseFloat(y.innerHTML.replace('$', '').replace('NA', '0.00'))
						) {
							shouldSwitch = true
							break
						}
					} else if (dir == 'dsc') {
						if (
							parseFloat(x.innerHTML.replace('$', '').replace('NA', '0.00')) <
							parseFloat(y.innerHTML.replace('$', '').replace('NA', '0.00'))
						) {
							shouldSwitch = true
							break
						}
					}
				} else {
					if (dir == 'asc') {
						if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
							shouldSwitch = true
							break
						}
					} else if (dir == 'dsc') {
						if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
							shouldSwitch = true
							break
						}
					}
				}
			}
			if (shouldSwitch) {
				rows[i].parentNode.insertBefore(rows[i + 1], rows[i])
				switching = true
				switchCount++
			} else {
				if (switchCount == 0 && dir == 'asc') {
					dir = 'dsc'
					switching = true
				}
			}
		}
	}

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
				img.id = `image_${result.data[i].id}`
				img.classList.add('mb-6', 'w-full', 'cursor-pointer', 'images')
				img.width = 'auto'
				img.height = 'auto'
				img.onclick = imageSelect

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
				if (result.data[i].tcgplayer == undefined) {
					tdPrice.innerHTML = 'NA'
				} else if (result.data[i].tcgplayer.prices == undefined) {
					tdPrice.innerHTML = 'NA'
				} else if (result.data[i].tcgplayer.prices.normal) {
					if (result.data[i].tcgplayer.prices.normal.market) {
						tdPrice.innerHTML = `$${result.data[
							i
						].tcgplayer.prices.normal.market.toFixed(2)}`
					} else {
						;`$${result.data[i].tcgplayer.prices.normal.mid.toFixed(2)}`
					}
				} else if (result.data[i].tcgplayer.prices.holofoil) {
					if (result.data[i].tcgplayer.prices.holofoil.market) {
						tdPrice.innerHTML = `$${result.data[
							i
						].tcgplayer.prices.holofoil.market.toFixed(2)}`
					} else {
						;`$${result.data[i].tcgplayer.prices.holofoil.mid.toFixed(2)}`
					}
				} else if (result.data[i].tcgplayer.prices.reverseHolofoil) {
					if (result.data[i].tcgplayer.prices.reverseHolofoil.market) {
						tdPrice.innerHTML = `$${result.data[
							i
						].tcgplayer.prices.reverseHolofoil.market.toFixed(2)}`
					} else {
						;`$${result.data[i].tcgplayer.prices.reverseHolofoil.mid.toFixed(
							2
						)}`
					}
				} else if (result.data[i].tcgplayer.prices.unlimited) {
					if (result.data[i].tcgplayer.prices.unlimited.market) {
						tdPrice.innerHTML = `$${result.data[
							i
						].tcgplayer.prices.unlimited.market.toFixed(2)}`
					} else {
						;`$${result.data[i].tcgplayer.prices.unlimited.mid.toFixed(2)}`
					}
				} else if (result.data[i].tcgplayer.prices.unlimitedHolofoil) {
					if (result.data[i].tcgplayer.prices.unlimitedHolofoil.market) {
						tdPrice.innerHTML = `$${result.data[
							i
						].tcgplayer.prices.unlimitedHolofoil.market.toFixed(2)}`
					} else {
						;`$${result.data[i].tcgplayer.prices.unlimitedHolofoil.mid.toFixed(
							2
						)}`
					}
				} else {
					tdPrice.innerHTML = '$0.00'
				}
				tdPrice.classList.add(...classArray)
				tdPrice.classList.add('text-right')

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

	if (sortBtn) {
		sortBtn.addEventListener('click', () => {
			sortDiv.classList.toggle('hidden')
		})

		const sortSet = document.getElementById('sort-set')
		const sortName = document.getElementById('sort-name')
		const sortRarity = document.getElementById('sort-rarity')
		const sortTypes = document.getElementById('sort-types')
		const sortSupertype = document.getElementById('sort-supertype')
		const sortSubtypes = document.getElementById('sort-subtypes')
		const sortPrice = document.getElementById('sort-price')

		sortSet.addEventListener('click', function () {
			sortTable(0)
			sortDiv.classList.toggle('hidden')
		})
		sortName.addEventListener('click', function () {
			sortTable(2)
			sortDiv.classList.toggle('hidden')
		})
		sortRarity.addEventListener('click', function () {
			sortTable(3)
			sortDiv.classList.toggle('hidden')
		})
		sortTypes.addEventListener('click', function () {
			sortTable(4)
			sortDiv.classList.toggle('hidden')
		})
		sortSupertype.addEventListener('click', function () {
			sortTable(5)
			sortDiv.classList.toggle('hidden')
		})
		sortSubtypes.addEventListener('click', function () {
			sortTable(6)
			sortDiv.classList.toggle('hidden')
		})
		sortPrice.addEventListener('click', function () {
			sortTable(7)
			sortDiv.classList.toggle('hidden')
		})
	}

	// view button functionality
	const toggleView = () => {
		searchTable.classList.toggle('sm:flex')
		searchTable.classList.toggle('sm:hidden')
		showResultsImage.classList.toggle('sm:hidden')
		showResultsImage.classList.toggle('sm:grid')
		if (viewBtn.innerText == 'Table') {
			viewBtn.innerText = 'Image'
			sortBtn.classList.toggle('hidden')
		} else if (viewBtn.innerText == 'Image') {
			viewBtn.innerText = 'Table'
			sortBtn.classList.toggle('hidden')
		}
	}

	if (viewBtn) {
		viewBtn.addEventListener('click', toggleView)
	}
}

document.addEventListener('DOMContentLoaded', initApp)
