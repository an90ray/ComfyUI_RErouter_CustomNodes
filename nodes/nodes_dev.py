#====----Test1_DEV----====
class test1:

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "STR1": ("STRING", {"forceInput": True})
            },
            "optional": {
            "STR2": ("STRING", {"forceInput": True}),
            "STR3": ("STRING", {"forceInput": True})
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING",)
    RETURN_NAMES = ("STR1", "STR2", "STR3",)
    FUNCTION = "reroute"
    CATEGORY = "(RE)route"
	
    def reroute(self, STR1, STR2, STR3):
        return (STR1, STR2, STR3,)
#====----Test2_DEV----====
class re_reroute:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "MODEL_B": ("MODEL",),
                "CLIP_B": ("CLIP",),
                "VAE_B": ("VAE",),
                "MODEL_R": ("MODEL",),
                "CLIP_R": ("CLIP",),
                "VAE_R": ("VAE",),
                "EM_LAT": ("LATENT",),
                "UPSC": ("UPSCALE_MODEL",),
                "STR_p": ("STRING", {"forceInput": True}),
                "STR_n": ("STRING", {"forceInput": True}),
                "SEED": ("INT", {"forceInput": True}),
                "STP_T": ("INT", {"forceInput": True}),
                "STP_R": ("INT", {"forceInput": True}),
                "STP_U": ("INT", {"forceInput": True})
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "MODEL", "CLIP", "VAE", "LATENT", "UPSCALE_MODEL", "STRING", "STRING", "INT", "INT", "INT", "INT",)
    RETURN_NAMES = ("MODEL_B", "CLIP_B", "VAE_B", "MODEL_R", "CLIP_R", "VAE_R", "EM_LAT", "UPSC", "STR_p", "STR_n", "SEED", "STP_T", "STP_R", "STP_U",)
    FUNCTION = "reroute"
    CATEGORY = "(RE)route"
	
    def reroute(self, MODEL_B, CLIP_B, VAE_B, MODEL_R, CLIP_R, VAE_R, EM_LAT, UPSCALE_MODEL, STR_p, STR_n, SEED, STP_T, STP_R, STP_U):
        return (MODEL_B, CLIP_B, VAE_B, MODEL_R, CLIP_R, VAE_R, EM_LAT, UPSCALE_MODEL, STR_p, STR_n, SEED, STP_T, STP_R, STP_U,)
