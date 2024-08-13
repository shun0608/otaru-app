<script lang="ts">
	import { goto } from '$app/navigation';
	import { login } from '../../components/store/store';
	import { displayLoginMessage } from '../../components/store/store';
	import toast, { Toaster } from 'svelte-french-toast';

	let email: string = '';
	let password: string = '';

	async function handleLogin() {
		try {
			await login(email, password);
			displayLoginMessage.set(true);
			goto('/');
		} catch (e) {
			if (e instanceof Error) {
				toast.error(e.message);
			} else {
				toast.error('ログイン処理中にエラーが発生しました。再度ログインを行ってください。');
			}
		}
	}
</script>

<svelte:head>
	<title>ログイン</title>
	<meta name="description" content="ログイン" />
</svelte:head>

<Toaster />

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
		<button on:click={handleLogin}>ログイン</button>
	</form>
</div>
