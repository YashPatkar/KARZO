<template>
    <div id="main" class="p-2">
        <nav class="px-4 py-3 text-center justify-between flex ">
            <a href="#" class="flex items-center gap-3">
                <img src="https://imgs.search.brave.com/i0cLgzLijK2E3SsXIRw1FLLHMQcrr5rQ4OR_GuHxyLg/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzAzLzQzLzA0LzUz/LzM2MF9GXzM0MzA0/NTM2OF9uM0xTRklo/cUtPSnNOSHZ6MnFw/enJXNWpTZWZzcFI1/Uy5qcGc"
                    alt="logo" class=" rounded-full w-14 h-14">
                <h2 class="uppercase text-2xl font-bold">
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
                <div class="flex flex-col justify-center text-black px-[7%] py-[5%]">
                    <span class="text-2xl text-gray-800 font-medium">
                        Ride nahi mil rahi hai..? Hamare pas hai rides 🙌.
                    </span>
                    <h1 class="text-6xl font-bold mt-4">
                        Welcome You at
                        <span class="text-indigo-800">KARZO Services </span>Site.
                    </h1>
                    <p class="mt-4 text-gray-700">
                        Karzo is a ride sharing platform that connects riders and drivers. We are here to provide you
                        click here to get a ride or to drive. 👇
                    </p>
                    <div class="mt-6 flex items-center space-x-4">
                        <button class="bg-blue-700 text-black px-6 py-3 rounded-lg flex items-center">
                            Want a Ride ?
                        </button>
                        <button class="flex items-center text-black border border-gray-500 px-6 py-3 rounded-lg">

                            Want to Drive ?
                        </button>
                    </div>
                </div>
                <div class="relative w-full h-[68vh] overflow-hidden">
                    <img src="https://media.istockphoto.com/id/1312916025/vector/couple-on-motorbike-travelers-in-helmets-highway.jpg?s=2048x2048&w=is&k=20&c=kws2S5YjSh8lwkCl_NtvZdR47hus66xGjkpke_tkDlA="
                        alt="Image" class="w-full h-full object-cover object-top">
                </div>


            </section>
        </main>
    </div>
</template>