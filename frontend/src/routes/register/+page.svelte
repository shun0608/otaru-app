<script lang="ts">
	let name: string = '';
	let email: string = '';
	let password: string = '';

	async function register() {
		const res = await fetch('http://localhost:8000/register', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				name: name,
				email: email,
				password: password
			})
		});
		console.log(res);
	}
</script>

<svelte:head>
	<title>ユーザー登録</title>
	<meta name="description" content="ユーザー登録" />
</svelte:head>

<div>
	<h1>ユーザー登録</h1>
	<form>
		<div>
			<label for="name">ユーザーネーム</label>
			<input type="text" bind:value={name} />
		</div>
		<div>
			<label for="email">メールアドレス</label>
			<input type="mail" bind:value={email} />
		</div>
		<div>
			<label for="password">パスワード</label>
			<input type="password" bind:value={password} />
		</div>
		<button type="button" on:click={register}>ユーザー登録</button>
	</form>
</div>
