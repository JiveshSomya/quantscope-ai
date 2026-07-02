mod analytics;
mod models;
mod routes;
mod services;

use routes::create_router;

#[tokio::main]
async fn main() {

    let app = create_router();

    let listener =
        tokio::net::TcpListener::bind("0.0.0.0:8081")
            .await
            .unwrap();

    println!("🚀 Quant Engine Running");

    axum::serve(listener, app)
        .await
        .unwrap();
}