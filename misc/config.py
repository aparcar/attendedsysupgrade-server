# where to store created images
# STORE_PATH="/var/asu/public/store",

# disable test and debug features
TESTING = False
DEBUG = True

# where to find the ImageBuildes
UPSTREAM_URL = "https://downloads.cdn.openwrt.org"

# supported versions
VERSIONS = {
    "metadata_version": 1,
    "branches": [
        {
            "name": "snapshot",
            "enabled": True,
            "versions": ["snapshot"],
            "git_branch": "master",
            "path": "snapshots",
            "path_packages": "snapshots/packages",
            "pubkey": "RWS1BD5w+adc3j2Hqg9+b66CvLR7NlHbsj7wjNVj0XGt/othDgIAOJS+",
            "updates": "dev",
            "repos": ["base", "packages", "luci", "routing", "telephony", "freifunk"],
            "extra_repos": {
                "lime-packages": "https://feed.libremesh.org/master",
                "lime-profiles": "https://feed.libremesh.org/profiles",
            },
            "targets": {
                "apm821xx/nand": "powerpc_464fp",
                "apm821xx/sata": "powerpc_464fp",
                "arc770/generic": "arc_arc700",
                "archs38/generic": "arc_archs",
                "armvirt/32": "arm_cortex-a15_neon-vfpv4",
                "armvirt/64": "aarch64_cortex-a53",
                "at91/sam9x": "arm_arm926ej-s",
                "at91/sama5": "arm_cortex-a5_vfpv4",
                "ath25/generic": "mips_mips32",
                "ath79/generic": "mips_24kc",
                "ath79/mikrotik": "mips_24kc",
                "ath79/nand": "mips_24kc",
                "ath79/tiny": "mips_24kc",
                "bcm27xx/bcm2708": "arm_arm1176jzf-s_vfp",
                "bcm27xx/bcm2709": "arm_cortex-a7_neon-vfpv4",
                "bcm27xx/bcm2710": "aarch64_cortex-a53",
                "bcm27xx/bcm2711": "aarch64_cortex-a72",
                "bcm47xx/generic": "mipsel_mips32",
                "bcm47xx/legacy": "mipsel_mips32",
                "bcm47xx/mips74k": "mipsel_74kc",
                "bcm53xx/generic": "arm_cortex-a9",
                "bcm63xx/generic": "mips_mips32",
                "bcm63xx/smp": "mips_mips32",
                "gemini/generic": "arm_fa526",
                "imx6/generic": "arm_cortex-a9_neon",
                "ipq40xx/generic": "arm_cortex-a7_neon-vfpv4",
                "ipq40xx/mikrotik": "arm_cortex-a7_neon-vfpv4",
                "ipq806x/generic": "arm_cortex-a15_neon-vfpv4",
                "kirkwood/generic": "arm_xscale",
                "lantiq/ase": "mips_mips32",
                "lantiq/xrx200": "mips_24kc",
                "lantiq/xway": "mips_24kc",
                "lantiq/xway_legacy": "mips_24kc",
                "layerscape/armv7": "arm_cortex-a7_neon-vfpv4",
                "layerscape/armv8_64b": "aarch64_generic",
                "malta/be": "mips_24kc",
                "mediatek/mt7622": "aarch64_cortex-a53",
                "mediatek/mt7623": "arm_cortex-a7_neon-vfpv4",
                "mediatek/mt7629": "arm_cortex-a7",
                "mpc85xx/p1010": "powerpc_8540",
                "mpc85xx/p1020": "powerpc_8540",
                "mpc85xx/p2020": "powerpc_8540",
                "mvebu/cortexa53": "aarch64_cortex-a53",
                "mvebu/cortexa72": "aarch64_cortex-a72",
                "mvebu/cortexa9": "arm_cortex-a9_vfpv3-d16",
                "mxs/generic": "arm_arm926ej-s",
                "octeon/generic": "mips64_octeonplus",
                "octeontx/generic": "aarch64_generic",
                "omap/generic": "arm_cortex-a8_vfpv3",
                "oxnas/ox820": "arm_mpcore",
                "pistachio/generic": "mipsel_24kc_24kf",
                "ramips/mt7620": "mipsel_24kc",
                "ramips/mt7621": "mipsel_24kc",
                "ramips/mt76x8": "mipsel_24kc",
                "ramips/rt288x": "mipsel_24kc",
                "ramips/rt305x": "mipsel_24kc",
                "ramips/rt3883": "mipsel_74kc",
                "realtek/generic": "mips_4kec",
                "rockchip/armv8": "aarch64_generic",
                "sunxi/cortexa53": "aarch64_cortex-a53",
                "sunxi/cortexa7": "arm_cortex-a7_neon-vfpv4",
                "sunxi/cortexa8": "arm_cortex-a8_vfpv3",
                "tegra/generic": "arm_cortex-a9_vfpv3-d16",
                "x86/64": "x86_64",
                "x86/generic": "i386_pentium4",
                "x86/geode": "i386_pentium-mmx",
                "x86/legacy": "i386_pentium-mmx",
                "zynq/generic": "arm_cortex-a9_neon",
            },
        },
        {
            "name": "19.07",
            "enabled": True,
            "eol": "2020-01-01",
            "versions": [
                "19.07.6",
                "19.07.5",
            ],
            "git_branch": "openwrt-19.07",
            "path": "releases/{version}",
            "path_packages": "releases/packages-{branch}",
            "pubkey": "RWT5S53W/rrJY9BiIod3JF04AZ/eU1xDpVOb+rjZzAQBEcoETGx8BXEK",
            "release_date": "2020-01-31",
            "updates": "bugs",
            "repos": ["base", "packages", "luci", "routing", "telephony"],
            "extra_repos": {
                "lime-packages": "https://feed.libremesh.org/master",
                "lime-profiles": "https://feed.libremesh.org/profiles",
            },
            "targets": {
                "apm821xx/nand": "powerpc_464fp",
                "apm821xx/sata": "powerpc_464fp",
                "ar71xx/generic": "mips_24kc",
                "ar71xx/mikrotik": "mips_24kc",
                "ar71xx/nand": "mips_24kc",
                "ar71xx/tiny": "mips_24kc",
                "arc770/generic": "arc_arc700",
                "archs38/generic": "arc_archs",
                "armvirt/32": "arm_cortex-a15_neon-vfpv4",
                "armvirt/64": "aarch64_generic",
                "at91/sam9x": "arm_arm926ej-s",
                "at91/sama5": "arm_cortex-a5_vfpv4",
                "ath25/generic": "mips_mips32",
                "ath79/generic": "mips_24kc",
                "ath79/nand": "mips_24kc",
                "ath79/tiny": "mips_24kc",
                "bcm53xx/generic": "arm_cortex-a9",
                "brcm2708/bcm2708": "arm_arm1176jzf-s_vfp",
                "brcm2708/bcm2709": "arm_cortex-a7_neon-vfpv4",
                "brcm2708/bcm2710": "aarch64_cortex-a53",
                "brcm47xx/generic": "mipsel_mips32",
                "brcm47xx/legacy": "mipsel_mips32",
                "brcm47xx/mips74k": "mipsel_74kc",
                "brcm63xx/generic": "mips_mips32",
                "brcm63xx/smp": "mips_mips32",
                "cns3xxx/generic": "arm_mpcore_vfp",
                "gemini/generic": "arm_fa526",
                "imx6/generic": "arm_cortex-a9_neon",
                "ipq40xx/generic": "arm_cortex-a7_neon-vfpv4",
                "ipq806x/generic": "arm_cortex-a15_neon-vfpv4",
                "kirkwood/generic": "arm_xscale",
                "lantiq/ase": "mips_mips32",
                "lantiq/falcon": "mips_24kc",
                "lantiq/xrx200": "mips_24kc",
                "lantiq/xway": "mips_24kc",
                "lantiq/xway_legacy": "mips_24kc",
                "layerscape/armv7": "arm_cortex-a7_neon-vfpv4",
                "layerscape/armv8_64b": "aarch64_generic",
                "malta/be": "mips_24kc",
                "mediatek/mt7622": "aarch64_cortex-a53",
                "mediatek/mt7623": "arm_cortex-a7_neon-vfpv4",
                "mpc85xx/generic": "powerpc_8540",
                "mpc85xx/p1020": "powerpc_8540",
                "mpc85xx/p2020": "powerpc_8540",
                "mvebu/cortexa53": "aarch64_cortex-a53",
                "mvebu/cortexa72": "aarch64_cortex-a72",
                "mvebu/cortexa9": "arm_cortex-a9_vfpv3-d16",
                "mxs/generic": "arm_arm926ej-s",
                "octeon/generic": "mips64_octeonplus",
                "octeontx/generic": "aarch64_generic",
                "omap/generic": "arm_cortex-a8_vfpv3",
                "oxnas/ox820": "arm_mpcore",
                "pistachio/generic": "mipsel_24kc_24kf",
                "ramips/mt7620": "mipsel_24kc",
                "ramips/mt7621": "mipsel_24kc",
                "ramips/mt76x8": "mipsel_24kc",
                "ramips/rt288x": "mipsel_24kc",
                "ramips/rt305x": "mipsel_24kc",
                "ramips/rt3883": "mipsel_74kc",
                "rb532/generic": "mipsel_mips32",
                "samsung/s5pv210": "arm_cortex-a8_neon",
                "sunxi/cortexa53": "aarch64_cortex-a53",
                "sunxi/cortexa7": "arm_cortex-a7_neon-vfpv4",
                "sunxi/cortexa8": "arm_cortex-a8_vfpv3",
                "tegra/generic": "arm_cortex-a9_vfpv3-d16",
                "x86/64": "x86_64",
                "x86/generic": "i386_pentium4",
                "x86/geode": "i386_pentium",
                "x86/legacy": "i386_pentium",
                "zynq/generic": "arm_cortex-a9_neon",
            },
        },
    ],
}
