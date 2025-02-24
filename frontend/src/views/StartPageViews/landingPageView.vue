<template>
    <div id="main" class="p-2">
        <nav class="px-4 py-3 text-center justify-between flex ">
            <a href="#" class="flex items-center gap-3 px-5">
                <h2 class="uppercase text-4xl font-bold bg-red-600 text-white font-sens p-2 rounded-sm">
                    karzo
                </h2>
            </a>
            <div class=" grid grid-cols-4 gap-5 p-2 rounded-xl items-center px-5 text-[20px]">
                <a href="#" class="capitalize">
                    Features
                </a>
                <a href="#" class="capitalize">
                    About
                </a>
                <a href="#" class="capitalize">
                    Services
                </a>
                <a href="#" class="capitalize">
                    Roles
                </a>
            </div>
            <div class="flex gap-5 px-3">
                <a href="#">
                    <button
                        class="border-2  border-black hover:border-gray-400 hover:text-gray-700 p-3 rounded-xl text-black ">Want
                        a Ride</button>
                </a>
                <a href="#">
                    <button
                        class="border-2  border-black hover:border-gray-400 hover:text-gray-700 p-3 rounded-xl text-black ">Want
                        to Drive</button>
                </a>
            </div>
        </nav>

        <main class="h-screen">
            <section class="h-[80%] grid grid-cols-1 md:grid-cols-2 gap-5 p-5">
                <div class="flex flex-col justify-center text-black pt-[10%] px-[9%] py-[5%]">
                    <span class="text-2xl text-gray-800 font-medium">
                        Ride nahi mil rahi hai..? Hamare pas hai rides 🙌.
                    </span>
                    <h1 class="text-6xl font-bold mt-4">
                        Welcome You at
                        <span class="text-indigo-800">KARZO Services </span>Site.
                    </h1>
                    <p class="mt-6 text-gray-700 w-[80%]">
                        Karzo is a ride sharing platform that connects riders and drivers. We are here to provide you
                        click here to get a ride or to drive. 👇
                    </p>
                    <div class="mt-9 flex items-center space-x-4">
                        <button class="bg-blue-700 text-white text-xl px-8 py-5 rounded-lg flex items-center">
                            Want a Ride ?
                        </button>
                        <button
                            class="flex items-center text-black text-xl border border-gray-500 px-8 py-5 rounded-lg">

                            Want to Drive ?
                        </button>
                    </div>
                </div>
                <div class="relative w-full h-[74vh] overflow-hidden pb-9 items-center">
                    <img src="https://media.istockphoto.com/id/1312916025/vector/couple-on-motorbike-travelers-in-helmets-highway.jpg?s=2048x2048&w=is&k=20&c=kws2S5YjSh8lwkCl_NtvZdR47hus66xGjkpke_tkDlA="
                        alt="Image" class="w-[80vw] h-[90vh] object-cover object-top ">
                </div>


            </section>
            <section class="h-full gap-5 p-5 text-center bg-orange-300 flex flex-col justify-center">
    <div class="mx-auto mt-10 mb-14 max-w-[800px] text-center lg:mb-16">
        <h2 class="mb-6 text-4xl font-bold text-black dark:text-white sm:text-5xl md:text-6xl md:leading-tight">
            Amazing Features to Make Your Work Easier
        </h2>
        <p class="text-base text-gray-700 dark:text-gray-300">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis tortor eros. Donec vitae tortor lacus. Phasellus aliquam ante in maximus.
        </p>
    </div>
    <div class="bg-blue-300 w-full max-w-[80%] mx-auto p-6 rounded-lg shadow-lg flex-grow h-40">
        <p class="text-white text-center text-lg font-semibold">
            Your content goes here! This space can be used for showcasing specific features or services.
        </p>
    </div>
</section>


        </main>
    </div>
</template>