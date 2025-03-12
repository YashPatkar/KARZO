<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="main bg-gradient-to-r from-blue-100 to-pink-100 min-h-screen">
        <!-- Navbar -->
        <nav class="flex justify-between items-center p-4 text-black shadow-md bg-white">
            <div class="flex items-center gap-2">
                <img src="https://imgs.search.brave.com/Ix0Mr6LI1hkvcoTZRErIzNd_74Vv5jz04QsuznqT1RE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9kMmo2/ZGJxMGV1eDBiZy5j/bG91ZGZyb250Lm5l/dC9pbWFnZXMvMjgy/MDEyOTQvMTQ2OTUz/NjQzMC5qcGc"
                    alt="Logo" class="h-14 w-14">
                <h2 class="text-2xl font-semibold">Karzo</h2>
            </div>
            <div class="hidden md:flex items-center gap-10 text-lg cursor-pointer">
                <h3 class="hover:text-gray-700 hover:-translate-y-3 transition duration-300">Events</h3>
                <h3 class="hover:text-gray-700 hover:-translate-y-3 transition duration-300">Users</h3>
                <h3 class="hover:text-gray-700 hover:-translate-y-3 transition duration-300">Feedback</h3>
                <h3 class="hover:text-gray-700 hover:-translate-y-3 transition duration-300">Blogs</h3>
                <h3 class="hover:text-gray-700 hover:-translate-y-3 transition duration-300">Safety</h3>
            </div>
            <div class="flex items-center gap-4">
                <RouterLink :to="{ name: 'DRegisterView' }">
                    <button class="border-2 border-black text-black hover:border-slate-600 px-4 py-2 rounded-md hover:bg-pink-700 hover:text-white transition">Driver Login/Signup</button>
                </RouterLink>
                <button class="border-2 border-black text-black hover:border-slate-600 px-4 py-2 rounded-md hover:bg-pink-700 hover:text-white transition">Passenger Login/Signup</button>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="flex flex-col lg:flex-row items-center justify-between p-6 lg:p-12 mx-auto max-w-7xl">

            <!-- Left Text Content -->
            <div class="max-w-md py-5">
                <h1 class="text-7xl font-bold mb-6 leading-tight">
                    Project management <br> tips & trends, delivered.
                </h1>
                <p class="text-gray-600 mb-6">
                    Join productivity experts from around the world and receive WriteClick—the Karzo Blog Newsletter.
                </p>
                <div class="flex items-center gap-2">
                    <input type="email" placeholder="Enter email"
                        class="border border-gray-300 px-4 py-3 rounded-lg w-64">
                    <button class="bg-pink-500 text-white px-6 py-3 rounded-lg hover:bg-pink-600">Subscribe</button>
                </div>
            </div>

            <!-- Right Image Card -->
            <div class="lg:mt-0 max-w-xl">
                <div class="bg-white rounded-lg shadow-lg overflow-hidden">
                    <img src="https://clickup.com/blog/wp-content/uploads/2024/09/Chat-Blog-Image.png" alt="Karzo Blog"
                        class="w-full">
                    <div class="p-4">
                        <h3 class="text-xl font-semibold">Chat Is Broken. We’re Fixing It.</h3>
                        <div class="flex items-center mt-2 text-gray-500 text-sm">
                            <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Author"
                                class="h-8 w-8 rounded-full mr-2">
                            <span>Zeb Evans</span>
                            <span class="ml-auto flex items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 8v4l3 3"></path>
                                </svg>
                                Max 1 min read
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Articles Section -->
        <section class="p-10">
            <h2 class="flex items-center text-2xl font-semibold gap-3 ">
                <i class="fa-regular fa-map bg-pink-500 p-4 rounded-2xl"></i>
                Top Events
            </h2>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-6">
                <!-- First Row -->
                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">ANNOUNCEMENTS</p>
                        <h3 class="text-xl font-bold mt-2">Chat Is Broken. We’re Fixing It.</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">ANNOUNCEMENTS</p>
                        <h3 class="text-xl font-bold mt-2">Chat Is Broken. We’re Fixing It.</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">ANNOUNCEMENTS</p>
                        <h3 class="text-xl font-bold mt-2">Chat Is Broken. We’re Fixing It.</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>

                <!-- Second Row -->
                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">ANNOUNCEMENTS</p>
                        <h3 class="text-xl font-bold mt-2">Chat Is Broken. We’re Fixing It.</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">ANNOUNCEMENTS</p>
                        <h3 class="text-xl font-bold mt-2">Chat Is Broken. We’re Fixing It.</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">ANNOUNCEMENTS</p>
                        <h3 class="text-xl font-bold mt-2">Chat Is Broken. We’re Fixing It.</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="p-10 lg:p-20">
            <h2 class="text-3xl font-bold mb-6">User Feedback</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div class="p-6 border rounded-lg shadow-md bg-white">
                    <div class="flex items-center space-x-4">
                        <img src="https://randomuser.me/api/portraits/women/1.jpg" alt="User Image"
                            class="w-14 h-14 rounded-full object-cover" />
                        <div>
                            <h3 class="text-lg font-semibold">Alice Johnson</h3>
                            <p class="text-yellow-500">⭐⭐⭐⭐⭐</p>
                        </div>
                    </div>
                    <p class="mt-4 text-gray-700">
                        Amazing service! The rides are super convenient and affordable.
                    </p>
                </div>

                <div class="p-6 border rounded-lg shadow-md bg-white">
                    <div class="flex items-center space-x-4">
                        <img src="https://randomuser.me/api/portraits/men/2.jpg" alt="User Image"
                            class="w-14 h-14 rounded-full object-cover" />
                        <div>
                            <h3 class="text-lg font-semibold">Michael Brown</h3>
                            <p class="text-yellow-500">⭐⭐⭐⭐</p>
                        </div>
                    </div>
                    <p class="mt-4 text-gray-700">
                        Great experience, but I wish there were more drivers available.
                    </p>
                </div>

                <div class="p-6 border rounded-lg shadow-md bg-white">
                    <div class="flex items-center space-x-4">
                        <img src="https://randomuser.me/api/portraits/women/3.jpg" alt="User Image"
                            class="w-14 h-14 rounded-full object-cover" />
                        <div>
                            <h3 class="text-lg font-semibold">Sophia Lee</h3>
                            <p class="text-yellow-500">⭐⭐⭐⭐⭐</p>
                        </div>
                    </div>
                    <p class="mt-4 text-gray-700">
                        Absolutely love the app! The booking process is smooth and easy.
                    </p>
                </div>
            </div>
        </section>

        <section class="p-10 lg:p-20 text-center relative">
  <h2 class="text-3xl font-bold mb-6">Latest Blogs & Insights</h2>
  <p class="text-lg text-gray-600 mb-10">
    Stay updated with expert opinions, industry trends, and the latest news from our team.
  </p>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <!-- Blog 1 -->
    <div class="flex flex-col md:flex-row items-center border-2 border-gray-400 backdrop-blur-md p-6 rounded-lg shadow-xl">
      <img src="https://imgs.search.brave.com/59qNrg_Isrs2nR6cV81iim8DTN58A6bNxJvBvTmu_YE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNjUx/MjcwMzExL3Bob3Rv/L2NoaGF0cmFwYXRp/LXNoaXZhamktcmFp/bHdheS1zdGF0aW9u/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1JblF0a3NpTnkx/aC11czBlcFc1Wl94/STJzQzh2VDhvWE5s/d002cjVuc0VvPQ" alt="Blog Image" class="w-full md:w-1/2 h-56 object-cover rounded-lg">
      <div class="p-6 text-left">
        <h3 class="text-xl font-semibold">The Future of Ridesharing</h3>
        <p class="text-gray-600 mt-2">
          The ridesharing industry is evolving rapidly with AI and electric vehicles playing a major role.
          Companies are focusing on safety measures, eco-friendly rides, and seamless customer experiences.
          As urban mobility demands grow, integrating smart technology will be crucial for the next phase of ridesharing.
        </p>
        <p class="text-gray-500 text-sm mt-2">😄 By John Doe | March 10, 2025</p>
      </div>
    </div>

    <!-- Blog 2 -->
    <div class="flex flex-col md:flex-row items-center border-2 border-gray-400 backdrop-blur-md p-6 rounded-lg shadow-xl">
      <img src="https://imgs.search.brave.com/59qNrg_Isrs2nR6cV81iim8DTN58A6bNxJvBvTmu_YE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNjUx/MjcwMzExL3Bob3Rv/L2NoaGF0cmFwYXRp/LXNoaXZhamktcmFp/bHdheS1zdGF0aW9u/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1JblF0a3NpTnkx/aC11czBlcFc1Wl94/STJzQzh2VDhvWE5s/d002cjVuc0VvPQ" alt="Blog Image" class="w-full md:w-1/2 h-56 object-cover rounded-lg">
      <div class="p-6 text-left">
        <h3 class="text-xl font-semibold">Smart City Transportation</h3>
        <p class="text-gray-600 mt-2">
          Smart cities are integrating intelligent transportation systems to reduce congestion and pollution.
          Automated public transport, data-driven traffic management, and sustainable ride options are shaping urban mobility.
          The future holds AI-driven solutions that will make commuting more efficient and affordable.
        </p>
        <p class="text-gray-500 text-sm mt-2">😄 By Jane Smith | March 8, 2025</p>
      </div>
    </div>

    <!-- Blog 3 -->
    <div class="flex flex-col md:flex-row items-center border-2 border-gray-400 backdrop-blur-md p-6 rounded-lg shadow-xl">
      <img src="https://imgs.search.brave.com/59qNrg_Isrs2nR6cV81iim8DTN58A6bNxJvBvTmu_YE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNjUx/MjcwMzExL3Bob3Rv/L2NoaGF0cmFwYXRp/LXNoaXZhamktcmFp/bHdheS1zdGF0aW9u/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1JblF0a3NpTnkx/aC11czBlcFc1Wl94/STJzQzh2VDhvWE5s/d002cjVuc0VvPQ" alt="Blog Image" class="w-full md:w-1/2 h-56 object-cover rounded-lg">
      <div class="p-6 text-left">
        <h3 class="text-xl font-semibold">Maximizing Driver Earnings</h3>
        <p class="text-gray-600 mt-2">
          Rideshare drivers can increase earnings by optimizing their working hours, choosing high-demand locations, and utilizing incentives.
          Learning passenger trends and leveraging in-app features help maximize efficiency.
          Future trends suggest better pay models and benefits for rideshare drivers.
        </p>
        <p class="text-gray-500 text-sm mt-2">😄 By Alex Brown | March 5, 2025</p>
      </div>
    </div>

    <!-- Blog 4 -->
    <div class="flex flex-col md:flex-row items-center border-2 border-gray-400 backdrop-blur-md p-6 rounded-lg shadow-xl">
      <img src="https://imgs.search.brave.com/59qNrg_Isrs2nR6cV81iim8DTN58A6bNxJvBvTmu_YE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNjUx/MjcwMzExL3Bob3Rv/L2NoaGF0cmFwYXRp/LXNoaXZhamktcmFp/bHdheS1zdGF0aW9u/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1JblF0a3NpTnkx/aC11czBlcFc1Wl94/STJzQzh2VDhvWE5s/d002cjVuc0VvPQ" alt="Blog Image" class="w-full md:w-1/2 h-56 object-cover rounded-lg">
      <div class="p-6 text-left">
        <h3 class="text-xl font-semibold">Ridesharing vs Traditional Taxis</h3>
        <p class="text-gray-600 mt-2">
          While traditional taxis have long been a reliable mode of transport, ridesharing apps offer flexibility, affordability, and real-time tracking.
          The competition is leading to improved services, but regulatory challenges remain a key factor.
          Passenger safety, pricing models, and driver benefits are crucial in shaping the industry's future.
        </p>
        <p class="text-gray-500 text-sm mt-2">😄 By Lisa Green | March 2, 2025</p>
      </div>
    </div>
  </div>
</section>


    </div>
</template>
