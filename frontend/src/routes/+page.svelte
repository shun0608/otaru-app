<script lang="ts">
	import { onMount } from 'svelte';
	import maplibregl from 'maplibre-gl';
	import 'maplibre-gl/dist/maplibre-gl.css';
	import toast, { Toaster } from 'svelte-french-toast';
	import { displayLoginMessage } from '../components/store/store';
	import { displayRegisterMessage } from '../components/store/store';

	let map: maplibregl.Map;

	onMount(() => {
		if ($displayLoginMessage) {
			toast.success('ログインしました');
			displayLoginMessage.set(false);
		} else if ($displayRegisterMessage) {
			toast.success('ユーザー登録が完了しました');
			displayRegisterMessage.set(false);
		}

		map = new maplibregl.Map({
			container: 'map',
			zoom: 5,
			center: [138, 37],
			minZoom: 5,
			maxZoom: 18,
			maxBounds: [122, 20, 154, 50],
			style: {
				version: 8,
				sources: {
					osm: {
						type: 'raster',
						tiles: ['https://tile.openstreetmap.org/{z}/{x}/{y}.png'],
						maxzoom: 19,
						tileSize: 256,
						attribution:
							'&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
					}
				},
				layers: [
					{
						id: 'osm-layer',
						source: 'osm',
						type: 'raster'
					}
				]
			}
		});
		let popup = new maplibregl.Popup({
			offset: 25, // ポップアップの位置
			closeButton: false // 閉じるボタンの表示
		}).setText('テストマーカー');
		let marker = new maplibregl.Marker()
			.setLngLat([139.70356, 35.65901])
			.setPopup(popup)
			.addTo(map);
	});
</script>

<svelt:head>
	<title>小樽観光マップ</title>
	<meta name="description" content="小樽の観光マップ" />
</svelt:head>

<Toaster />

<div id="map" style="height: 100svh;"></div>
