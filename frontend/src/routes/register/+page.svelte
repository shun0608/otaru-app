<script lang="ts">
	let name: string = '';
	let email: string = '';
	let password: string = '';
	let message: string = '';

	async function fetchUser() {
		const response = await fetch('http://localhost:8000/register', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				name,
				email,
				password
			})
		});
		return response;
	}

	async function register() {
		try {
			const registrationResult = await fetchUser();
			const data = await registrationResult.json();
			if (data.detail == 'REGISTER_USER_ALREADY_EXISTS') {
				throw new Error('入力されたメールアドレスは既に登録されています。');
			}
			// ここに、登録後の処理を記載する
		} catch (e) {
			if (e instanceof Error) {
				message = e.message;
			} else {
				message =
					'登録処理中に予期しないエラーが発生しました。お手数ですが、再度登録処理を行ってください。';
			}
		}
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

	<p>
		{message}
	</p>
</div>
