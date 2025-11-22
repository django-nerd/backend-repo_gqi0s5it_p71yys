import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Any, Dict, List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----- Base & Health -----
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI Backend!"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from the backend API!"}

# ----- Site configuration served from backend -----
SITE_CONFIG: Dict[str, Any] = {
  "site": {
    "name": "Custom Treasures",
    "url": "https://custom-treasures.example",
    "description": "An online boutique specializing in personalized, engraved and photo-customizable gifts.",
    "language": "en-US",
    "visual": {
      "brandColors": {
        "primary": "#D4A373",
        "secondary": "#8ECAE6",
        "accent": "#B5838D",
        "bg": "#FFFDF9",
        "muted": "#F3ECE6",
        "text": "#1F1A17"
      },
      "typeScale": {
        "h1": "36px",
        "h2": "28px",
        "h3": "20px",
        "body": "16px",
        "small": "13px"
      },
      "fontFamilies": {
        "headline": "'Poppins', system-ui, Arial",
        "body": "'Inter', system-ui, Arial"
      },
      "cornerRadius": "12px",
      "shadow": "0 8px 24px rgba(0,0,0,0.08)",
      "imageStyle": {
        "cover": True,
        "rounded": True,
        "altOverlay": "soft-gradient"
      },
      "animations": {
        "micro": "translateY(4px) ease-out 120ms",
        "hoverLift": "translateY(-6px) ease-out 180ms",
        "fade": "opacity 200ms ease-in"
      }
    },
    "globalHeader": {
      "logo": {
        "src": "/assets/logo-customtreasures.svg",
        "alt": "Custom Treasures logo"
      },
      "topNav": [
        { "label": "Home", "route": "/" },
        { "label": "Shop", "route": "/shop" },
        { "label": "Collections", "route": "/lookbook" },
        { "label": "Blog", "route": "/blog" },
        { "label": "About", "route": "/about" }
      ],
      "utilityNav": [
        { "label": "Search", "action": "openSearch" },
        { "label": "Wishlist", "route": "/wishlist" },
        { "label": "Cart", "route": "/cart" },
        { "label": "Account", "route": "/account" }
      ],
      "behavior": {
        "sticky": True,
        "shrinkOnScroll": True,
        "mobileHamburger": True
      }
    },
    "globalFooter": {
      "columns": [
        {
          "title": "Shop",
          "links": [
            { "label": "Personalized Mugs", "route": "/shop?category=mugs" },
            { "label": "Photo Gifts", "route": "/shop?category=photo" },
            { "label": "Engraved Jewelry", "route": "/shop?category=jewelry" },
            { "label": "Custom Decor", "route": "/shop?category=decor" }
          ]
        },
        {
          "title": "Company",
          "links": [
            { "label": "About", "route": "/about" },
            { "label": "Press", "route": "/press" },
            { "label": "Careers", "route": "/careers" }
          ]
        },
        {
          "title": "Help",
          "links": [
            { "label": "FAQ", "route": "/faq" },
            { "label": "Shipping", "route": "/shipping" },
            { "label": "Contact", "route": "/contact" }
          ]
        }
      ],
      "copyright": "© 2025 Custom Treasures",
      "social": [
        { "name": "Instagram", "url": "https://instagram.com/customtreasures", "ariaLabel": "Custom Treures on Instagram" },
        { "name": "TikTok", "url": "https://tiktok.com/@customtreasures", "ariaLabel": "Custom Treasures on TikTok" }
      ]
    },
    "pages": [
      {
        "route": "/",
        "title": "Home",
        "meta": {
          "title": "Custom Treasures — Personalized & Custom Gifts",
          "description": "Unique personalized gifts: custom mugs, engraved jewelry, photo gifts, LED lamps and more."
        },
        "layout": {
          "hero": {
            "type": "carousel",
            "slides": [
              {
                "image": "/assets/hero-gift1.jpg",
                "headline": "Make Every Gift Personal",
                "subheadline": "Custom mugs, engraved jewelry and photo keepsakes.",
                "cta": { "label": "Shop Gifts", "route": "/shop" }
              },
              {
                "image": "/assets/hero-gift2.jpg",
                "headline": "Memories That Last",
                "subheadline": "Turn your photos into timeless treasures.",
                "cta": { "label": "Photo Gifts", "route": "/shop?category=photo" }
              }
            ],
            "autoplay": True,
            "autoplayInterval": 6000,
            "accessibility": { "pauseOnFocus": True, "ariaLabel": "Homepage hero carousel" }
          },
          "featureRow": [
            { "icon": "truck", "headline": "Fast Shipping", "text": "Delivery across Romania." },
            { "icon": "gift", "headline": "Gift Packaging", "text": "Premium gift-ready packaging options." },
            { "icon": "support", "headline": "Customer Support", "text": "We're here to help daily." }
          ],
          "collectionsShowcase": {
            "title": "Personalized Collections",
            "collections": [
              { "title": "Engraved Jewelry", "image": "/assets/collection-jewelry.jpg", "route": "/shop?collection=jewelry" },
              { "title": "Custom Mugs", "image": "/assets/collection-mugs.jpg", "route": "/shop?collection=mugs" },
              { "title": "Photo Gifts", "image": "/assets/collection-photo.jpg", "route": "/shop?collection=photo" }
            ]
          },
          "instagramStrip": {
            "title": "From Instagram",
            "images": ["/assets/insta1.jpg", "/assets/insta2.jpg", "/assets/insta3.jpg"],
            "cta": { "label": "Follow @customtreasures", "url": "https://instagram.com/customtreasures" }
          }
        }
      },
      {
        "route": "/shop",
        "title": "Shop / Catalog",
        "meta": {
          "title": "Shop Personalized Gifts • Custom Treasures",
          "description": "Browse personalized gifts by category, filter and sort."
        },
        "layout": {
          "leftSidebar": {
            "components": [
              { "type": "search", "placeholder": "Search gifts, e.g. 'mug', 'bracelet'" },
              {
                "type": "filters",
                "filters": [
                  { "name": "Category", "type": "checkbox", "options": ["Mugs", "Photo Gifts", "Jewelry", "Decor"] },
                  { "name": "Color", "type": "swatch", "options": ["Black", "White", "Gold", "Rose Gold", "Silver"] },
                  { "name": "Price", "type": "range", "min": 20, "max": 500 }
                ]
              },
              { "type": "collectionsList" }
            ]
          },
          "productGrid": {
            "columnsDesktop": 4,
            "columnsTablet": 2,
            "columnsMobile": 1,
            "card": {
              "imageRatio": "4:5",
              "fields": ["image", "productName", "price", "badge", "quickActions"],
              "quickActions": [
                { "action": "quickView", "label": "Quick view" },
                { "action": "wishlist", "label": "♡" },
                { "action": "addToCart", "label": "Add to cart" }
              ]
            },
            "sortOptions": ["Featured", "Price: Low → High", "Price: High → Low", "New Arrivals"]
          },
          "emptyState": {
            "message": "No products match your filters.",
            "cta": { "label": "Reset filters", "action": "resetFilters" }
          }
        },
        "mockData": {
          "pagination": { "page": 1, "perPage": 20, "total": 42 },
          "products": [
            {
              "id": "SKU-MUG-001",
              "name": "Personalized Photo Mug",
              "category": "Mugs",
              "price": "49,00 RON",
              "images": ["/assets/products/mug1.jpg"],
              "labels": ["Best seller"],
              "shortDescription": "Upload your image and add text for a unique mug.",
              "availability": "In stock"
            },
            {
              "id": "SKU-JWL-002",
              "name": "Engraved Name Bracelet",
              "category": "Jewelry",
              "price": "119,00 RON",
              "images": ["/assets/products/bracelet1.jpg"],
              "labels": ["New"],
              "shortDescription": "Stainless steel bracelet customized with any name.",
              "availability": "In stock"
            }
          ]
        }
      },
      {
        "route": "/product/:productId",
        "title": "Product Detail",
        "meta": {
          "title": "Product • Custom Treasures",
          "description": "Personalized gift details and customization options."
        },
        "layout": {
          "main": {
            "left": {
              "component": "imageGallery",
              "props": {
                "images": "product.images",
                "zoom": True,
                "altTemplate": "Image of {product.name}"
              }
            },
            "right": {
              "component": "productInfo",
              "fields": [
                "name",
                "sku",
                "rating",
                "price",
                "shortDescription",
                "variants",
                "customizationFields",
                "sizeGuideLink",
                "quantityPicker",
                { "component": "addToCart", "label": "Add to cart" }
              ]
            }
          },
          "belowFold": {
            "tabs": [
              { "label": "Description", "content": "Full product description and customization details." },
              { "label": "Details", "content": "Materials, dimensions and care instructions." },
              { "label": "Shipping & Returns", "content": "Shipping times, policies and return eligibility." },
              { "label": "Reviews", "content": [] }
            ],
            "relatedProductsCarousel": { "title": "You may also like", "limit": 8 }
          }
        }
      },
      {
        "route": "/cart",
        "title": "Cart",
        "meta": { "title": "Cart • Custom Treasures" },
        "layout": {
          "main": {
            "cartTable": {
              "columns": ["image", "name", "price", "qty", "subtotal", "remove"],
              "editableQty": True
            },
            "summaryCard": {
              "subTotal": "calculated",
              "shipping": "calculated",
              "total": "calculated",
              "checkoutButton": { "label": "Proceed to Checkout", "route": "/checkout" }
            }
          }
        }
      },
      {
        "route": "/checkout",
        "title": "Checkout",
        "meta": { "title": "Checkout • Custom Treasures" },
        "layout": {
          "main": {
            "form": {
              "sections": [
                {
                  "title": "Shipping Details",
                  "fields": [
                    { "name": "fullName", "type": "text", "label": "Full name" },
                    { "name": "email", "type": "email", "label": "Email" },
                    { "name": "address", "type": "textarea", "label": "Address" }
                  ]
                },
                {
                  "title": "Shipping Method",
                  "options": [
                    { "id": "standard", "label": "Standard (2–5 days)", "price": "14,00 RON" },
                    { "id": "express", "label": "Express (1–2 days)", "price": "29,00 RON" }
                  ]
                },
                {
                  "title": "Payment",
                  "fields": [
                    { "name": "cardNumber", "type": "text", "label": "Card number" },
                    { "name": "expiry", "type": "text", "label": "Expiry (MM/YY)" },
                    { "name": "cvc", "type": "text", "label": "CVC" }
                  ]
                }
              ],
              "cta": { "label": "Place Order", "action": "submitOrder" }
            }
          }
        }
      },
      {
        "route": "/order/CONFIRM",
        "title": "Order Confirmation",
        "meta": { "title": "Order Confirmed • Custom Treasures" },
        "layout": {
          "main": {
            "headline": "Order Confirmed 🎁",
            "orderSummary": {
              "orderId": "ORD-2025-0001",
              "items": "list of items",
              "total": "calculated",
              "note": "Thank you for your order!"
            },
            "nextSteps": [
              "A confirmation email has been sent.",
              "We'll notify you when your package ships."
            ],
            "cta": { "label": "Back to Shop", "route": "/shop" }
          }
        }
      }
    ]
  }
}

@app.get("/api/site", response_model=dict)
def get_site_config() -> Dict[str, Any]:
    return SITE_CONFIG

# Products API (mocked from site config)

def _get_mock_products() -> List[Dict[str, Any]]:
    pages = SITE_CONFIG.get("site", {}).get("pages", [])
    for p in pages:
        if p.get("route") == "/shop":
            data = p.get("mockData", {})
            return data.get("products", [])
    return []

@app.get("/api/products", response_model=dict)
def list_products(q: str | None = None, category: str | None = None) -> Dict[str, Any]:
    products = _get_mock_products()
    filtered = products
    if q:
        ql = q.lower()
        filtered = [p for p in filtered if ql in p.get("name", "").lower() or ql in p.get("shortDescription", "").lower()]
    if category:
        filtered = [p for p in filtered if p.get("category", "").lower() == category.lower()]
    return {"items": filtered, "count": len(filtered)}

@app.get("/api/products/{product_id}", response_model=dict)
def get_product(product_id: str) -> Dict[str, Any]:
    products = _get_mock_products()
    for p in products:
        if p.get("id") == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")


@app.get("/test")
def test_database():
    """Test endpoint to check if database is available and accessible"""
    response = {
        "backend": "✅ Running",
        "database": "❌ Not Available",
        "database_url": None,
        "database_name": None,
        "connection_status": "Not Connected",
        "collections": []
    }

    try:
        from database import db
        if db is not None:
            response["database"] = "✅ Available"
            response["database_url"] = "✅ Configured"
            response["database_name"] = db.name if hasattr(db, 'name') else "✅ Connected"
            response["connection_status"] = "Connected"
            try:
                collections = db.list_collection_names()
                response["collections"] = collections[:10]
                response["database"] = "✅ Connected & Working"
            except Exception as e:
                response["database"] = f"⚠️  Connected but Error: {str(e)[:50]}"
        else:
            response["database"] = "⚠️  Available but not initialized"
    except ImportError:
        response["database"] = "❌ Database module not found (run enable-database first)"
    except Exception as e:
        response["database"] = f"❌ Error: {str(e)[:50]}"

    # Check environment variables
    response["database_url"] = "✅ Set" if os.getenv("DATABASE_URL") else "❌ Not Set"
    response["database_name"] = "✅ Set" if os.getenv("DATABASE_NAME") else "❌ Not Set"

    return response


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
