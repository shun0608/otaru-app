<script lang="ts">
	let email: string = '';
	let password: string = '';
	let message: string = '';
	$: fetchBody = `username=${email}&password=${password}`;

	async function fetchUser() {
		const response = await fetch('http://localhost:8000/login', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded'
			},
			credentials: 'include',
			body: fetchBody
		});
		return response;
	}

	async function login() {
		try {
			const loginResult = await fetchUser();
			if (loginResult.status === 204) {
				message = 'ログインに成功しました';
			} else {
				throw new Error(
					'ログイン処理中に何らかのエラーが発生しました。再度ログイン処理を行ってください。'
				);
			}
		} catch (e) {
			if (e instanceof Error) {
				message = e.message;
			} else {
				message =
					'ログイン処理中に何らかのエラーが発生しました。再度ログイン処理を行ってください。';
			}
		}
	}
</script>

<svelte:head>
	<title>ログイン</title>
	<meta name="description" content="ログイン" />
</svelte:head>

<div>
	<h1>ログイン</h1>
	<form>
		<div>
			<label for="username">メールアドレス</label>
			<input type="mail" bind:value={email} />
		</div>
		<div>
			<label for="password">パスワード</label>
			<input type="password" bind:value={password} />
		</div>
		<button on:click={login}>ログイン</button>
	</form>
</div>

<p>
	{message}
</p>
