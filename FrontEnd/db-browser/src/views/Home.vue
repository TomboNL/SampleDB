<template>
    <span>
        <hello-world msg='MVDP'></hello-world>
    </span>
</template>

<script>
import HelloWorld from '@/components/HelloWorld';

export default {
    name: 'home',
    components: {
        HelloWorld
    }
};
</script>